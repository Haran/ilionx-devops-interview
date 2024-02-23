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

1. Task 1: Building and containerising a Spring Boot application
   1. [Preparation and sanity checks](doc/TASK1.md:1)
   2. [Packing to docker, simple](doc/TASK1.md:28)
   3. [Packing to docker, multistage, with compilation](doc/TASK1.md:40)
   4. Using Gitlab CI/CD
   5. Using Github Actions
2. Task 2
3. Task 3
