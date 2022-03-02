# CATO Command Line Client

This package provides the command line interface (CLI) client for the CATO 
system. Succesful usage of the CATO cli will require a functional CATO system 
to which you have access and can reach via your local network/Internet 
connection. This package  really provides two primary items:

1. The CATO command line interface `catocli`
1. The CATOClient Python object.

This package and associated scripts are written exclusively for Python 3 ONLY.

We are operating under a fairly obvious assumption that you have acccess to
a functional CATO system in order to use this command line interface. 

## Installation
Since the CLI is distributed as a PIP package, installation of the CATO CLI is 
simple. You are strongly advised to download the copy of the CATO CLI that is 
directly associated to your CATO instance.

### Downloading CATO CLI
This is under development. Until this is completed, you will be issued the CLI
manually by a CyberPoint team member.

### Installation Example
The CATO CLI package name will include the version of CATO it is compatible with as 
follows:

    cato_cli-<VERSION>-py3-none-any.whl

Once you have downloaded the CATO CLI package, you can install with the following
syntax which will install the `catocli` script to `/usr/local/bin/catocli`.

    developer@ubuntu:~/$ sudo pip3 install cato_cli-0.16.3_developer-py3-none-any.whl
 

If you'd like to make this accessible for your account, or if you lack sudo privileges, then running the command without sudo may work as well which should install the `catocli` script to `~/.local/bin/catocli`.

    developer@ubuntu:~/$ pip3 install cato_cli-0.16.3_developer-py3-none-any.whl

Here is an example of installation on Ubuntu:

    developer@ubuntu:~/$ sudo pip install cato_cli-0.16.3_developer-py3-none-any.whl
    Processing ./cato_cli-0.16.3_developer-py3-none-any.whl
    Installing collected packages: cato-cli
    Successfully installed cato-cli-0.16.3-developer

We assume you are familiar with the CATO system already and do not include any 
tutorials on CATO or how it works. For more information on these please consult
a CyberPoint team member. Of most importance, you should be aware of your status
as an operator or mission director when attempting certain actions such as 
approval of operations.

## Development
If you are going to develop for the CATO CLI you are strongly advised to follow
the same environment as our team:

* Ubuntu Desktop 18.04 LTS
* Visual Studio Code

As long as you have make installed, you can setup your development environment 
with the following command:

    make develop    

Be aware, this will install over 1GB of extra files due to the TEXLive fonts
that are required. 

## Building
The following content within the build section is for those who have a copy of the source code bundle. Running the `'make package'` command should create a `dist/` folder, containing the `wheel` (.whl) file used during the aforementioned installation process. We provide an example on building catocli on Windows 10 here:

    PS C:\Users\developer\source\repos\cato\cato-cli> make package
    running bdist_wheel
    running build
    running build_py
    creating build
    creating build\lib
    creating build\lib\catocli
    copying catocli\catoclient.py -> build\lib\catocli
    copying catocli\__init__.py -> build\lib\catocli
    running build_scripts
    creating build\scripts-3.8
    copying scripts\catocli -> build\scripts-3.8
    ...TRUNCATED...
    24462 INFO: Building PYZ because PYZ-00.toc is non existent
    24465 INFO: Building PYZ (ZlibArchive) C:\Users\developer\source\repos\cato\cato-cli\build\catocli\PYZ-00.pyz
    26522 INFO: Building PYZ (ZlibArchive) C:\Users\developer\source\repos\cato\cato-cli\build\catocli\PYZ-00.pyz completed successfully.
    26562 INFO: checking PKG
    26564 INFO: Building PKG because PKG-00.toc is non existent
    26564 INFO: Building PKG (CArchive) PKG-00.pkg
    35271 INFO: Building PKG (CArchive) PKG-00.pkg completed successfully.
    35292 INFO: Bootloader c:\users\developer\appdata\local\programs\python\python38\lib\site-packages\PyInstaller\bootloader\Windows-64bit\run.exe
    35293 INFO: checking EXE
    35293 INFO: Building EXE because EXE-00.toc is non existent
    35294 INFO: Building EXE from EXE-00.toc
    35309 INFO: Appending archive to EXE C:\Users\developer\source\repos\cato\cato-cli\dist\catocli.exe
    35355 INFO: Building EXE from EXE-00.toc completed successfully.

### Building Stand-Alone Binary
This project includes an automatic call to pyinstaller to produce a stand-alone
binary if invoked. This is the ideal build configuration if you do not wish to 
worry about missing package requirements. The syntax to build and stand-alone 
version of the CATO CLI is:

    make binary

Here is an example output from this build command

    sysadmin@cato:~/workspace/cato/cato-cli$ make binary
    27 INFO: PyInstaller: 4.1
    27 INFO: Python: 3.6.9
    27 INFO: Platform: Linux-5.4.0-80-generic-x86_64-with-Ubuntu-18.04-bionic
    27 INFO: wrote /home/sysadmin/workspace/cato/cato-cli/catocli.spec
    30 INFO: UPX is not available.
    31 INFO: Extending PYTHONPATH with paths
    ['/home/sysadmin/workspace/cato/cato-cli',
    '/home/sysadmin/workspace/cato/cato-cli/catocli',
    '/home/sysadmin/workspace/cato/cato-cli']
    36 INFO: checking Analysis
    36 INFO: Building Analysis because Analysis-00.toc is non existent
    36 INFO: Initializing module dependency graph...
    37 INFO: Caching module graph hooks...
    41 INFO: Analyzing base_library.zip ...
    2221 INFO: Caching module dependency graph...
    2288 INFO: running Analysis Analysis-00.toc
    2325 INFO: Analyzing /home/sysadmin/workspace/cato/cato-cli/scripts/catocli
    2451 INFO: Processing pre-safe import module hook six.moves from '/home/sysadmin/.local/lib/python3.6/site-packages/PyInstaller/hooks/pre_safe_import_module/hook-six.moves.py'.
    4911 INFO: Processing pre-find module path hook 
    TRUNCATED
    19484 INFO: checking PKG
    19484 INFO: Building PKG because PKG-00.toc is non existent
    19484 INFO: Building PKG (CArchive) PKG-00.pkg
    34993 INFO: Building PKG (CArchive) PKG-00.pkg completed successfully.
    34997 INFO: Bootloader /home/sysadmin/.local/lib/python3.6/site-packages/PyInstaller/bootloader/Linux-64bit/run
    34997 INFO: checking EXE
    34997 INFO: Building EXE because EXE-00.toc is non existent
    34998 INFO: Building EXE from EXE-00.toc
    34998 INFO: Appending archive to ELF section in EXE /home/sysadmin/workspace/cato/cato-cli/dist/catocli
    35200 INFO: Building EXE from EXE-00.toc completed successfully.

The resulting binary will be found in the dist directory and be named catocli

    sysadmin@cato:~/workspace/cato/cato-cli$ ls dist/
    catocli  cato_cli-0.16.3_sysadmin-py3-none-any.whl  cato-cli-0.16.3-sysadmin.tar.gz

You should be aware, this binary can be greater than forty (40) megabytes.

## CLI 
We discuss examples on using the CATO CLI script in this section. The CLI is 
designed to make your life easier when interacting with CATO. Installation of 
the PIP package will create an executable script in your local system path named:

`/usr/local/bin/catocli`

You can print the arguments for this script using the following syntax:

    catocli -h

You should note uninstallation of this package will remove this script. You 
do not need to worry about removing on your own.

The CLI arguments are explicitly designed to be easy. Of special note are the 
first three (3) positional arguments from the help text:

    usage: catocli [-h] [-a APPLIANCE] [-cm CAMPAIGN] [-A] [-c CUSTOMER]
                [-C CONFIGFILE] [-f OUTPUTFORMAT] [-F OUTPUTFILTER]
                [-H HOMEDIR] [-i INPUTDIR] [-I IDENTIFIER] [-j JSON]
                [-L LOGLEVEL] [-op OPERATION] [-o OPPFOR] [-O OUTPUTFILE]
                [-p CATOPASS] [-q] [-t TYPE] [-T TEMPLATE] [-u CATOUSER]
                [-U URL] [-v VALUE] [-z ZONE]
                ACTION NOUN [SUBJECT [SUBJECT ...]]

    positional arguments:
    ACTION                Specify action for CATO cli.
    NOUN                  Specify object in CATO to focus on (e.g. operation,
                            target, finding)
    SUBJECT               Specify a target subject for your action and noun

    optional arguments:
    -h, --help            show this help message and exit
    -a APPLIANCE, --appliance APPLIANCE
                            Specify customer appliance
    -cm CAMPAIGN, --campaign CAMPAIGN
                            Specify customer operation campaign (INTEGER)
    -A, --activate        Ensure new target(s) are activated.
    -c CUSTOMER, --customer CUSTOMER
                            Specify customer identifer (INTEGER)
    -C CONFIGFILE, --configfile CONFIGFILE
                            Specify an alternate CATO configuration filename.
                            Default is ~/.cato/catocli.ini
    -f OUTPUTFORMAT, --outputformat OUTPUTFORMAT
                            Specify output format
    -F OUTPUTFILTER, --outputfilter OUTPUTFILTER
                            Specify output format
    -H HOMEDIR, --homedir HOMEDIR
                            Specify an alternate CATO home directory. Default is
                            ~/.cato
    -i INPUTDIR, --inputdir INPUTDIR
                            Specify the input directory
    -I IDENTIFIER, --identifier IDENTIFIER
                            Specify the noun subject identifier
    -j JSON, --json JSON  Specify json for use in create operation
    -L LOGLEVEL, --loglevel LOGLEVEL
                            Specify alternate logging level. (Default is NONE)
    -op OPERATION, --operation OPERATION
                            Specify operation title
    -o OPPFOR, --oppfor OPPFOR
                            Specify oppposing force identifer (INTEGER)
    -O OUTPUTFILE, --outputfile OUTPUTFILE
                            Specify output location
    -p CATOPASS, --catopass CATOPASS
                            Specify CATO system user password
    -q, --quiet           Supress logging. Default is FALSE
    -t TYPE, --type TYPE  Specify CATO object value type
    -T TEMPLATE, --template TEMPLATE
                            Specify operational template
    -u CATOUSER, --catouser CATOUSER
                            Specify CATO system usernme
    -U URL, --url URL     Specify CATO server URL at runtime
    -v VALUE, --value VALUE
                            Specify value to use for add action(s)
    -z ZONE, --zone ZONE  Specify target zone to use

Since CATO is designed to 'do stuff', these positional arguments can be 
explained as follows (in order):

* ACTION is the thing you want CATO to actually do for you
* NOUN is the target of your ACTION like CREATE a TARGET
* SUBJECT is the ultimate focus of your NOUN and ACTION. Such as CREATE TARGET 10.0.0.1

While you will be able to perform many actions using just these 3 arguments if
you properly setup your CATOCLIENT.INI file, the remaining arguments supported 
by the CLI are required for combinations of these actions such `-z` for specifying
a ZONE for a newly created target. or `-a` for specifying an appliance. 

By in large, only lowercase values should be used AND it is important to only 
specify singular values for each ACTION or NOUN even though it might be tempting
to use the plural version(s). For example,

        catocli approve operation

NOT

        catocli approve operations

## CATOCLI Binary
If you choose to build the catocli stand-alone binary you are responsible for 
transporting this to your target system. This will be located in which ever 
folder you choose to drop into.

### Supported Actions
The currently supported ACTION values are:

* `approve`    this will approve/authorize the execution of an operation
* `autorun`      this will run an operation automatically. Do this CAREFULLY
* `create`       this will create an object (e.g. target, operation)
* `list`         this will find objects and list them on stdout. Should be used with the search to limit to what items or columns you want
* `login`        this will login to CATO and generate/save an access token
* `ping`         this is a way to check and see if your CATO server is active
* `run`          this will run a command including a Django command on your CATO system

### Supported Nouns
The CLI supports different noun values based on the action type. The simplest way
to determine which noun to use or NOT use will be through experience.

### catoclient.ini
Usage of the CATO CLI will create a properties file in your home directory.
This file is meant to save certain properties and arguments that simplify making
calls into CATO especially on a repeated basis. The location of this file is:

    $HOME/.cato

It is important that you protect this file with proper access permissions as it
will hold authentication information for your CATO system(s). You are free to never
set these properties if you deem the risk unacceptable. An example of the default 
INI file that is created is as follows:

    [server]
    url = https://192.168.1.10
    apipath = api/v1
    authorization = 8f88b8f0ddd1aa4b42884d93ce611bff234f911ce2f2a2cf6862c996835a3dd4
    verify_ssl = false
    sshport = 22
    timeout = 30
    exec_container = compose_cato-portal-api_1

    [auth]
    catouser = mission_a
    catopass = password
    sshuser = sysadmin
    sshpass = PASSWORD

    [history]
    last_oppfor = 2
    last_appliance = 0

Take special note of the authorization token and the auth section(s). The first 
time you authenticate to CATO you MUST supply a username and password if you do 
not specify them in the INI file like the previous example. When you successfully
authenticate, the authorization token will be saved for quick re-usage. If your 
token as saved in the INI file has expired you will be automatically reprompted
to specify a password.

NOTE: This approach may change; do not rely on this as a permanent feature!

Uninstallation of the PIP package will NOT remove this file. You are 
responsible for removing this INI file your own.

### Output
The CLI supports a limited number of output formats but defaults to CSV. You can
change the format with the `-f` and `-O` arguments:

* `-f` will change the output format (Supported formats: `csv`, `json`, `pandas`)
* `-O` changes the output destination (defaults to stdout)

You can use the `-q` argument suppress output logging which will appear prior to
actual output.

### Output Filtering
You can use the `-F` argument to filter output object fields to a specific set of keys.

    catocli list customer -F id,name,nickname,date_joined

    ,id,name,nickname,date_joined
    0,1,CyberPoint International,CPI,2020-10-11T14:24:51.453036Z
    1,2,The Acme Corporation,ACORP,2020-10-11T14:24:51.642121Z
    2,3,Garage Incorporated,G,2020-10-11T14:24:51.900639Z

You need to run the query you are interested in first to get a complete listing of
the fields that are provided before you can filter the output like we show in this
example.

### Examples

We provide specific examples in this section. When in doubt, you should `ping` your CATO 
instance so that you can first confirm it is active and second so you can cache your login
to CATO so you don't need to re-type your username and password.

    sysadmin@cato:~/workspace/cato/cato-cli$ catocli ping https://192.168.1.10 -u mission_a -p PASSWORD 
    05/28/2021 10:03:17 AM reading CATO client properties
    05/28/2021 10:03:17 AM full path to CATO client configuration file is /home/sysadmin/.cato/catoclient.ini
    05/28/2021 10:03:17 AM all read
    05/28/2021 10:03:17 AM creating CATOClient object
    05/28/2021 10:03:17 AM set verify SSL to False
    05/28/2021 10:03:17 AM set waiting period to 22
    05/28/2021 10:03:17 AM setting SSH user --> sysadmin
    05/28/2021 10:03:17 AM setting SSH password
    05/28/2021 10:03:17 AM set authorization token from options file
    05/28/2021 10:03:17 AM authorization token still unset
    05/28/2021 10:03:17 AM using CATO URL specified in property file https://127.0.0.1
    05/28/2021 10:03:17 AM using CATO URL specified on command line https://192.168.1.10
    05/28/2021 10:03:17 AM set path to CATOClient options as /home/sysadmin/.cato/catoclient.ini
    05/28/2021 10:03:17 AM unmodified CATO URL---> https://192.168.1.10
    05/28/2021 10:03:17 AM base CATO URL---> https://192.168.1.10/
    05/28/2021 10:03:17 AM using CATO authorization URL: https://192.168.1.10/auth/login/
    05/28/2021 10:03:17 AM using CATO server URL https://192.168.1.10/api/v1/
    05/28/2021 10:03:17 AM processing action ping
    05/28/2021 10:03:17 AM executing method <bound method CATOClient.ping of <catocli.catoclient.CATOClient object at 0x7f41da988748>>
    05/28/2021 10:03:17 AM ping CATO server auth endpoint https://192.168.1.10/auth/login/ now
    05/28/2021 10:03:17 AM 401
    https://192.168.1.10/api/v1/ --> pong


#### List Objects
List opposing forces (registered customers):

    catocli list customer

List ALL targets on your CATO system

    catocli list target

List ALL targets on your CATO system for a specific opposing force/customer

    catocli list target -c 'CyberPoint International'

List ALL targets on your CATO system for a specific opposingforce/customer identifier '1'

    catocli list target -c 1

List ALL findings on your CATO system

    catocli list finding

List ALL operations on your CATO system

    catocli list operation

#### Create Objects

When creating an object, the target entity to be created can either be specified via the SUBJECT or within a JSON object passed with the '-j' flag. If the target values are specified by both the SUBJECT and JSON entities, the SUBJECT entity will take priority and will be used to override whatever value is passed within the JSON object. Furthermore, any command line argument or flag specified will take priority and override anything that's specified within the JSON body.

Create a target

    catocli create target 192.168.1.123 -c 5 -f json -j '{"customer":5,"type":"ipaddress","active":true,"tags":[],"zone":5,"is_explicitly_aliased":false}'

Note: When working with operation creation, use the target value instead of the ID of the object that's used within the backend. The client should automatically resolve the target value to the target ID.

Create an operation

    catocli create operation 10.0.1.1 --campaign 23 --template 'Ping (Basic Ping)' --customer 5

Create an operation using JSON

    catocli create operation 10.0.1.1 -c 5 -j '{"campaign":23,"template":134,"reasoning":"New operation requested."}'

Creating the same operation for multiple targets

    catocli create operations 192.168.1.1,192.168.1.3 -c 5 -f json -j '{"campaign":23,"template":134,"reasoning":"New operation requested."}'