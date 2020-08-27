# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.define "centos" do |centos|
    centos.vm.box = "centos/7"
    centos.vm.hostname = "daidalos.khardix.cz"
  end

  config.vm.define "alpine" do |alpine|
    alpine.vm.box = "generic/alpine310"
    alpine.vm.hostname = "ikaros.khardix.cz"
  end

  config.vm.define "minecraft" do |minecraft|
    minecraft.vm.box = "centos/7"
    minecraft.vm.hostname = "mc.khardix.cz"

    minecraft.vm.provider :libvirt do |libvirt|
      libvirt.cpus = 4
      libvirt.memory = 6144
    end
  end

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "playbook.yml"
    ansible.compatibility_mode = "2.0"
    ansible.groups = {
      "minecraft" => ["minecraft"],
    }
    ansible.host_vars = {
      "alpine" => {
        "ansible_port": 443,

        # Vagrant sets only short host name on Alpine
        "override_fqdn" => "ikaros.khardix.cz",
      },
      "centos" => {
        "ansible_port": 443,
      },
      "minecraft" => {
        "ansible_port": 443,
      },
    }
  end
end
