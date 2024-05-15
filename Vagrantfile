Vagrant.configure("2") do |config|
  # Настройка nginx серверов
  (1..3).each do |i|
    config.vm.define "nginx#{i}" do |nginx|
      nginx.vm.box = "ubuntu/focal64"
      nginx.vm.network "private_network", ip: "192.168.50.10#{i}"
      nginx.vm.hostname = "nginx#{i}"
      nginx.vm.synced_folder ".", "/vagrant", disabled: true
      nginx.vm.provider "virtualbox" do |vb|
        vb.memory = "1024"
        vb.cpus = "2"
      end
      nginx.vm.provision "ansible" do |ansible|
        ansible.playbook = "nginx-setup.yml"
        ansible.groups = {
          "nginx_servers" => ["nginx#{i}"]
        }
      end
    end
  end

  # Настройка приложения
  config.vm.define "app" do |app|
    app.vm.box = "ubuntu/focal64"
    app.vm.network "private_network", ip: "192.168.50.200"
    app.vm.hostname = "app"
    app.vm.provider "virtualbox" do |vb|
      vb.memory = "2048"
      vb.cpus = "2"
    end
    app.vm.provision "ansible" do |ansible|
      ansible.playbook = "app-setup.yml"
    end
  end
end
