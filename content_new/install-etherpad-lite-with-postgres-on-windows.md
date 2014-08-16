Title: Setting up etherpad with postgres on Windows
Date: 2012-12-27T11:20:36
Tags: windows, postgres, node, etherpad


There don't seem to be any successful installation instructions for postgres on Windows. It's not that hard, but there are a couple things you need to do. 

I haven't gone through these instructions to make sure they work, but this is roughly what I've done to get my Postgres/Windows/Node/Etherpad working together:

 - Install git
 - Install node.js
 - Install python
     - add PYTHON as an env
 - Install postgres
     - add C:\Program Files\PostgreSQL\9.2\bin to your path
 - Download etherpad-lite with git
 - Run the etherpad-lite windows installer per the instructions
 - start etherpad-lite
     - make sure it works with the dirty DB before getting exotic
 - Set up postgres
     - npm install pg (will throw an error about msbuild version, but ignore that, the native JS drivers are installed)
     - add a user using pgadmin
     - add a DB using pgadmin and the user created a second ago
     - reconfigure to use postgres in the settings.json file
 -  Run start.bat to make sure it works
 - Turn down the log messages to only ERROR in the settings.json file.
 - Use [NSSM][2] to daemonize it, per the instructions [here][1].

Note that NSSM doesn't yet have stdout and stderr redirection built in. Thus, to start the daemon with these working, you have to create a little script like this: 

    @ECHO OFF
    @REM This runs etherpad with stdout and stderr getting redirected to special logs
    call D:\etherpad\etherpad-lite\start.bat >> D:\etherpad\etherpad-lite\logs\stdout.log 2>> D:\etherpad\etherpad-lite\logs\stderr.log


[1]: https://github.com/ether/etherpad-lite/wiki/How-to-deploy-Etherpad-Lite-as-a-service
[2]: http://nssm.cc/