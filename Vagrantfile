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

  $bootstrap = <<-BOOTSTRAP
  command -v apk && apk add python3 || :
  command -v dnf && dnf -y install python || :
  command -v yum && yum -y install python || :
  BOOTSTRAP

  config.vm.provision "shell", inline: $bootstrap
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "playbook.yml"
    ansible.compatibility_mode = "2.0"
    ansible.host_vars = {
      "alpine" => {
        # Vagrant sets only short host name on Alpine
        "override_fqdn" => "ikaros.khardix.cz",
      },
    }
  end
end
