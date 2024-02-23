For easier command running I've created a GNU `Makefile` with small recipes that work like aliases for ansible-playbook command.

### Ansible Docker installation in Vagrant VM

- Create `docker-playbook.yml`
- Pretty straightforward installation process

> I usually try to pin versions of software installed in order to preserve uniformity in the server and application landscape. As far as nothing was specified in task, it's left as-is.

### Ansible packing hello world application to docker image and running it

- Create `helloworld-playbook.yml`
- As long as I've already created multi-stage building process, it seems reasonable to handle it with Ansible, hence creating idempotent and reproducable scenario for build-and-run.
- Mandatory thing is to run containers with limited resources unless specified otherwise (for demonstartion purposes simple `cpus: 1, memory: 512M` seems to be enough)
