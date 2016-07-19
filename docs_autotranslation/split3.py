#!/usr/bin/env python
import os

guides = ['header','section_Git_and_Gerrit_Setup','section_Hacking_from_CLI','developing-app','alto/alto-developer-guide','armoury/odl-armoury-dev','bgpcep/odl-bgpcep-bgp-all-dev'
,'capwap/capwap-dev','controller/controller','didm/didm-dev','dlux/dlux-core-dev','iotdm/iotdm-dev','l2switch/l2switch-dev','lacp/lacp-dev.adoc','messaging4transport/messaging4transport-developer',
'controller/netconf/odl-netconf-dev','nic/nic-dev','nemo/odl-nemo-engine-dev','netide/netide-developer-guide','neutron/neutron','sdninterfaceapp/odl-sdninterfaceapp-all-dev',
'openflowjava/odl-openflowjava-protocol-dev','openflowplugin/odl-ofp-developer-guide','opflex/agent-ovs-dev','opflex/genie-dev','opflex/libopflex-dev',
'ovsdb/ovsdb-southbound-developer', #newly added guides
'ovsdb/ovsdb-openstack-developer','ovsdb/ovsdb-sfc-developer','ovsdb/ovsdb-hwvtep-developer',
'bgpcep/odl-bgpcep-pcep-all-dev','packetcable/packetcable-dev','sfc/sfc','sxp/odl-sxp-dev','tcpmd5/odl-tcpmd5-all-dev',
'topoprocessing/odl-topoprocessing-framework-dev','ttp/ttp-model-dev','ttp/ttp-cli-tools-dev','usc/odl-usc-channel-dev','vtn/vtn-dev','yangtools/yangtools',
'yang-push/odl-yang-push-dev']

header = open('header.rst','r')
text = header.read()
header.close()
file = open('index.rst','w')
file.write(text)
file.write('.. toctree:: \n')
file.write('	:maxdepth: 1 \n')
file.write('\n')
for i in range(1,len(guides)):
	file.write('	'+guides[i]+'\n')
file.close()