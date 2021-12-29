## 1. Use  already created internal-network for three VMs (VM1-VM3). VM1 has NAT and internal, VM2, VM3 – internal only interfaces.

![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m6/task_6.2/images/nat_port_forward.png)

## 2.Install and configure DHCP server on VM1.(3 ways: using VBoxManage, DNSMASQ and ISC-DHSPSERVER). You should use at least 2 of them

![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m6/task_6.2/images/dhcp_vb.png)

![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m6/task_6.2/images/dhcp_server_vb.png)

![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m6/task_6.2/images/dnsmasq_conf.png)

![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m6/task_6.2/images/dnsmasq_status.png)

## 3.Check VM2 and VM3  for obtaining  network addresses from DHCP server.

![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m6/task_6.2/images/ip_a_vm1.png)

![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m6/task_6.2/images/ip_a_vm2.png)

![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m6/task_6.2/images/ip_a_vm3.png)

![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m6/task_6.2/images/ping_google_vm1.png)

![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m6/task_6.2/images/ping_google_vm2.png)

![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m6/task_6.2/images/ping_google_vm3.png)

![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m6/task_6.2/images/ping_vm1_vm2.png)

![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m6/task_6.2/images/ping_vm1_vm3.png)

## 4.Using existed network for three VMs ( from p.1) install and configure DNS server on VM1. (You can use DNSMASQ, BIND9 or something else).

![](https://raw.githubusercontent.com/ViktorMarhitich/DevOps_online_Dnipro_2021Q4/main/m6/task_6.2/images/dns_config.png)