# Streamline operations on Vagrant-managed VMs
MACHINE := alpine centos
SSH_PORT := 443

# Do not particularly care about ruby warnings from Vagrant
export RUBYOPT=-W0

.PHONY: all idempotence clean
.PHONY: $(MACHINE)
.PHONY: %-login %-cleaned

# Spin up and provision all machines
all: $(foreach machine,$(MACHINE),.vagrant/machines/$(machine)/ssh-config)
# Log in to specific machine and spawn a root shell
alpine: alpine-login
centos: centos-login
# Re-provision all machines to test for script idempotence
idempotence: all
	vagrant provision | grep 'changed='
# Destroy the machines
clean: $(MACHINE:%=%-cleaned)

%-login: .vagrant/machines/%/ssh-config
	ssh -F$< -p$(SSH_PORT) -t $(@:%-login=%) -- sudo -s

.vagrant/machines/%/ssh-config: Vagrantfile
	vagrant up $(notdir $(@D))
	vagrant ssh-config $(notdir $(@D)) >$@

%-cleaned:
	$(RM) .vagrant/machines/$(@:%-cleaned=%)/ssh-config
	vagrant destroy --force $(@:%-cleaned=%)
