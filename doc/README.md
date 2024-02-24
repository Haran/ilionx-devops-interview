# Workflow log

This is basically a transcript of several `~/.bash_history` files, aggregated in markdown for more convenience with some comments, in order to demonstrate way of working and thinking

### Pseudo-mirror

1. Fork and clone locally
2. Create gitlab empty project to demonstrate ability to work with both platforms
    ```bash
    $ git remote add gitlab git@gitlab.com:olegs.capligins/ilionx-devops-interview.git
    $ git remote rename origin github
    $ git remote -v
      github  git@github.com:Haran/ilionx-devops-interview.git (fetch)
      github  git@github.com:Haran/ilionx-devops-interview.git (push)
      gitlab  git@gitlab.com:olegs.capligins/ilionx-devops-interview.git (fetch)
      gitlab  git@gitlab.com:olegs.capligins/ilionx-devops-interview.git (push)
    $ git push gitlab main
    ```

I know that repository mirroring exists, but here I prefer to have manual control with 2 git remotes.

### Tasks

1. **[Task 1](TASK1.md)**: Building and containerising a Spring Boot application
   1. [Preparation and sanity checks](TASK1.md#vagrant-and-application-sanity-check)
   2. [Packing to docker, simple](TASK1.md#packing-to-docker)
   3. [Packing to docker, multistage, with compilation](TASK1.md#multistage-packing)
   4. [Using Gitlab CI/CD](TASK1.md#gitlab-cicd)
   5. [Using Github Actions](TASK1.md#github-actions)
2. **[Task 2](TASK2.md)**: Ansible playbooks
   1. [Docker installation](TASK2.md#ansible-docker-installation-in-vagrant-vm)
   2. [Packing hello world application to docker image and running it](TASK2.md#ansible-packing-hello-world-application-to-docker-image-and-running-it)
   3. [System wide tweaks](TASK2.md#ansible-system-wide-tweaks)
3. **[Task 3](TASK3.md)**: Sunrise-Sunset application
   1. [Brainstorm](TASK3.md#thinking-out-loud)
   2. [Development](TASK3.md#development)
   3. [Possible vectors of improvement](TASK3.md#possible-vectors-of-improvement)
      > For instructions how to run, please check [README.md](../circadian/README.md)
