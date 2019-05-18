import logging

from cmdb.models import Host
from tabops.settings import DEFAULT_LOGGER, SALT_API_URL
from saltapi.salt_https_api import salt_api_token
from saltapi.salt_token_id import token_id


logger = logging.getLogger(DEFAULT_LOGGER)


def scan_host_job(tgt):
    """
    扫描客户端信息
    :return:
    """

    logger.info("获取Minion主机资产信息")
    # result = salt_api_token({'fun': 'grains.items', 'tgt': tgt, 'expr_form': 'list'},
    #                         SALT_API_URL, {'X-Auth-Token': token_id()}).CmdRun()['return'][0]
    result = salt_api_token({'fun': 'grains.items', 'tgt': tgt},
                            SALT_API_URL, {'X-Auth-Token': token_id()}).CmdRun()['return'][0]
    logger.info("扫描Minion数量为[%s]", len(result))
    logger.debug("Minions资产信息[%s]" % result)

    #  for scan all
    if tgt == '*':
        Host.objects.update(minion_status=0)

    for host in result:
        minionstatus = 1
        result[host]["ipv4"].remove('127.0.0.1')
        l_ip = None
        m_ip = None
        for ip in result[host]["ipv4"][::-1]:
            if "10.25.172" in ip or "172.188.2" in ip or "10.25.171" in ip or "172.188.1" in ip or "172.188.3" in ip:
                l_ip = ip
            if "10.25.178" in ip or "10.110.70" in ip or "10.25.177" in ip or "10.110.72" in ip or "10.110.73" in ip:
                m_ip = ip

        rs = Host.objects.filter(host_name=host)
        if len(rs) == 0:
            logger.info("新增主机:%s", host)

            device = Host(host_name=host,
                          lan_ip=l_ip,
                          man_ip=m_ip,
                          kernel=result[host]["kernel"] if 'kernel' in result[host] else "",
                          kernel_release=result[host]["kernelrelease"] if 'kernelrelease' in result[host] else "",
                          virtual=result[host]["virtual"] if 'virtual' in result[host] else "",
                          host=result[host]["host"] if 'host' in result[host] else "",
                          osrelease=result[host]["osrelease"] if 'osrelease' in result[host] else "",
                          saltversion=result[host]["saltversion"] if 'saltversion' in result[host] else "",
                          osfinger=result[host]["osfinger"] if 'osfinger' in result[host] else "",
                          os_family=result[host]["os_family"] if 'os_family' in result[host] else "",
                          system_serialnumber=result[host]['serialnumber'] if 'serialnumber' in result[
                              host] else "",
                          cpu_model=result[host]["cpu_model"] if 'cpu_model' in result[host] else "",
                          productname=result[host]['productname'] if "productname" in result[host]else"",
                          osarch=result[host]["osarch"] if 'osarch' in result[host] else "",
                          cpuarch=result[host]["cpuarch"] if 'cpuarch' in result[host] else "",
                          os=result[host]["os"] if 'os' in result[host] else "",
                          mem_total=result[host]["mem_total"] if 'mem_total' in result[host] else 0,
                          num_cpus=result[host]["num_cpus"] if 'num_cpus' in result[host] else 0,
                          minion_status=minionstatus,
                          roles=result[host]["roles"][0] if 'roles' in result[host] else "",
                          )
            device.save()
        else:
            entity = rs[0]
            logger.info("更新主机:%s", entity)
            entity.lan_ip = l_ip
            entity.man_ip = m_ip
            entity.kernel = result[host]["kernel"] if 'kernel' in result[host] else ""
            entity.kernel_release = result[host]["kernelrelease"] if 'kernelrelease' in result[host] else ""
            entity.virtual = result[host]["virtual"] if 'virtual' in result[host] else ""
            entity.host = result[host]["host"] if 'host' in result[host] else ""
            entity.osrelease = result[host]["osrelease"] if 'osrelease' in result[host] else ""
            entity.saltversion = result[host]["saltversion"] if 'saltversion' in result[host] else ""
            entity.osfinger = result[host]["osfinger"] if 'osfinger' in result[host] else ""
            entity.os_family = result[host]["os_family"] if 'os_family' in result[host] else ""
            entity.num_gpus = result[host]["num_gpus"] if 'num_gpus' in result[host] else 0
            entity.system_serialnumber = result[host]["serialnumber"] if 'serialnumber' in result[host] else ""
            entity.cpu_model = result[host]["cpu_model"] if 'cpu_model' in result[host] else ""
            entity.productname = result[host]["productname"] if 'productname' in result[host] else ""
            entity.osarch = result[host]["osarch"] if 'osarch' in result[host] else ""
            entity.cpuarch = result[host]["cpuarch"] if 'cpuarch' in result[host] else ""
            entity.os = result[host]["os"] if 'os' in result[host] else ""
            entity.mem_total = result[host]["mem_total"] if 'mem_total' in result[host] else 0
            entity.num_cpus = result[host]["num_cpus"] if 'num_cpus' in result[host] else 0
            entity.minion_status = minionstatus
            entity.roles = result[host]["roles"][0] if 'roles' in result[host] else ""
            entity.save()

