# File and Network Analysis

## Section 1. YARA:

### Step1: Setting Up the Malware Analysis Environment

![Screenshot 1](images/im1.png)
> Figure 1.0

![Screenshot 2](images/im2.png)
> Figure 1.1

### Step2: Downloading a Malware Sample – MalwareBaazar

![Screenshot 3](images/im3.png)
> Figure 1.2

![Screenshot 4](images/im4.png)
> Figure 1.3

![Screenshot 5](images/im5.png)
> Figure 1.4

![Screenshot 6](images/im6.png)
> Figure 1.5

Malware Source: https://bazaar.abuse.ch/sample/56e4cffe84730f0636cbcca1891576435e7503066d2925b58db47cacb3ae9fac/ 

### Step3: Extract the Malware Sample

Commands Used:

`cd` Downloads

`mv` 56e4cffe84730f0636cbcca1891576435e7503066d2925b58db47cacb3ae9fac.zip ~`/malware_lab`

`7z x` 56e4cffe84730f0636cbcca1891576435e7503066d2925b58db47cacb3ae9fac.zip

-pinfected

![Screenshot 7](images/im7.png)
> Figure 1.6

Note: For this screenshot above, I have two malware samples because one of them was empty so I had to download another one.

![Screenshot 8](images/im8.png)
> Figure 1.7

![Screenshot 9](images/im9.png)
> Figure 1.8

![Screenshot 10](images/im10.png)
> Figure 1.9

### Step4: Static Malware Analysis with YARA

Commands Used:

`strings` 708e19985a6322c3f7fc7f7088d5dc07b5bdc6e9a9be185fc389eb09.exe | less

`objdump` -x 708e19985a6322c3f7fc7f7088d5dc07b5bdc6e9a9be185fc389eb09.exe | `grep` -i import

`exiftool` 708e19985a6322c3f7fc7f7088d5dc07b5bdc6e9a9be185fc389eb09.exe

`binwalk` 708e19985a6322c3f7fc7f7088d5dc07b5bdc6e9a9be185fc389eb09.exe

`rabin2` 708e19985a6322c3f7fc7f7088d5dc07b5bdc6e9a9be185fc389eb09.exe

`rabin2` -i 708e19985a6322c3f7fc7f7088d5dc07b5bdc6e9a9be185fc389eb09.exe

![Screenshot 11](images/im11.png)
> Figure 2.0

![Screenshot 12](images/im12.png)
> Figure 2.1

![Screenshot 13](images/im13.png)
> Figure 2.2

![Screenshot 14](images/im14.png)
> Figure 2.3

![Screenshot 15](images/im15.png)
> Figure 2.4

![Screenshot 16](images/im16.png)
> Figure 2.5

![Screenshot 17](images/im17.png)
> Figure 2.6

![Screenshot 18](images/im18.png)
> Figure 2.7


During the analysis of the malware sample using tools such as `objdump` and `rabin2`, I noticed that mscoree.dll is mentioned in both. As I was unsure of what it is, I went ahead and did some research to find out what it is. This is a core component of the Microsoft .NET Framework. It is responsible for loading and initializing the Common Language Runtime (CLR), which is essential for executing .NET applications. Hence, the presence of mscoree.dll confirms that the sample is a .NET application.

Citation: https://www.fortect.com/fix-dll-errors/mscorlib-dll-errors-visual-studio/#:~:text=It%20stands%20for%20Microsoft%20Common,NET%20applications%20rely%20on.  

### Step5: The YARA Rule

![Screenshot 19](images/im19.png)
> Figure 2.8

### Step6: Screenshots of running the YARA Against the Malware Sample and YARA Rule file

Commands Used:

`yara` -s my_malware.`yara` 708e19985a6322c3f7fc7f7088d5dc07b5bdc6e9a9be185fc389eb09.exe

`yara` my_malware.`yara` 708e19985a6322c3f7fc7f7088d5dc07b5bdc6e9a9be185fc389eb09.exe

`sha256sum` 708e19985a6322c3f7fc7f7088d5dc07b5bdc6e9a9be185fc389eb09.exe


![Screenshot 20](images/im20.png)
> Figure 2.9

![Screenshot 21](images/im21.png)
> Figure 3.0

![Screenshot 22](images/im22.png)
> Figure 3.1


File Name: 708e19985a6322c3f7fc7f7088d5dc07b5bdc6e9a9be185fc389eb09.exe

SHA256 Hash: 708e198608b5b463224c3fb77fcf708b845d0c7b5dbc6e9cab9e185c489be089

## Section 2. Snort:

### Part1:

Commands Used:

`sudo` `apt-get` update

`sudo` `apt-get` install `snort`

`/etc/``snort`/`snort`.conf

`snort` -v

`sudo` `updatedb`

`locate` `snort`.lua

`ip addr`

`sudo` `nano` `/etc/``snort`/`snort`.lua

`ls` `/etc/``snort``/rules`

`sudo` `tar` -xvzf snort3-community-rules.`tar`.gz -c `/etc/``snort``/rules`

`sudo` `snort` -d -l `/var/log/``snort` -h 192.168.0.0`/24` -A console -c `/etc/``snort`/`snort`.lua

`sudo` `snort` -c `/etc/``snort`/`snort`.lua -I eth0 -A console

`sudo` `snort` -c `/etc/``snort`/`snort`.lua -I eth0


![Screenshot 23](images/im23.png)
> Figure 3.2

![Screenshot 24](images/im24.png)
> Figure 3.3

![Screenshot 25](images/im25.png)
> Figure 3.4

![Screenshot 26](images/im26.png)
> Figure 3.5

![Screenshot 27](images/im27.png)
> Figure 3.6

![Screenshot 28](images/im28.png)
> Figure 3.7

![Screenshot 29](images/im29.png)
> Figure 3.8

![Screenshot 30](images/im30.png)
> Figure 3.9

![Screenshot 31](images/im31.png)
> Figure 4.0

![Screenshot 32](images/im32.png)
> Figure 4.1

![Screenshot 33](images/im33.png)
> Figure 4.2

![Screenshot 34](images/im34.png)
> Figure 4.3

![Screenshot 35](images/im35.png)
> Figure 4.4

![Screenshot 36](images/im36.png)
> Figure 4.5

![Screenshot 37](images/im37.png)
> Figure 4.6

![Screenshot 38](images/im38.png)
> Figure 4.7

![Screenshot 39](images/im39.png)
> Figure 4.9

![Screenshot 40](images/im40.png)
> Figure 5.0

### Conclusion:

Commands used to get here as shown in figures 4.4 and 4.5:

`sudo` `snort` -c `/etc/``snort`/`snort`.lua -i eth0 -A console

However, after starting the process, I ran into fatal errors as shown in figure 4.4.

Error message includes unknown logger console. This is due to -A console option not being recognized.

Hence, to resolve this issue, I removed the ‘-A console’ to test if it works and it worked as shown in figure 4.5.

-c `/etc/``snort`/`snort`.lua tells `snort` to read the `snort` config file located at `/etc/``snort`/`snort`.lua

-i eth0 tells the network eth0 that `snort` should monitor

-A console is used to direct `snort` to output alerts to the console

### Part 2:

Commands Used:

`sudo` `nano` `/etc/``snort``/rules/local.rules`

`sudo` `nano` `/etc/``snort`/`snort`.lua

`sudo` `snort` -c `/etc/``snort`/`snort`.lua -R `/etc/``snort``/rules/local.rules` -i eth0 -l `/var/log/``snort`/

`ping` 192.168.0.105

`sudo` `cat` `/var/log/``snort``/alert_fast.txt`


![Screenshot 41](images/im41.png)
> Figure 5.1

![Screenshot 42](images/im42.png)
> Figure 5.2

![Screenshot 43](images/im43.png)
> Figure 5.3

![Screenshot 44](images/im44.png)
> Figure 5.4 Modfied the snort.lua file to direct the trigger logs into alert_fast.txt file in /var/log/snort directory

![Screenshot 45](images/im45.png)
> Figure 5.5

Here `sudo` `snort` -c `/etc/``snort`/`snort`.lua ran the command in root and specifies the config file for `snort`.lua.

-R `/etc/``snort``/rules/local.rules` loaded the custom rule file that I had initially implemented for trigger testing.

i eth0 tells `snort` to monitor traffic on the specific interface

l `/var/log/``snort`/ is used to set to directory where the `snort` will write its logs


![Screenshot 46](images/im46.png)
> Figure 5.6

![Screenshot 47](images/im47.png)
> Figure 5.7

![Screenshot 48](images/im48.png)
> Figure 5.8 Successfully triggered snort with pinging 192.168.0.105


### Part 3:

Commands Used:

`sudo` `snort` -c `/etc/``snort`/`snort`.lua -R `/etc/``snort``/rules/local.rules` -A alert_fast

`sudo` `nano` `/etc/``snort``/rules/local.rules`

`sudo` `cat` `/var/log/``snort``/alert_fast.txt`

![Screenshot 49](images/im49.png)
> Figure 5.9

![Screenshot 50](images/im50.png)
> Figure 6.0

![Screenshot 51](images/im51.png)
> Figure 6.1

![Screenshot 52](images/im52.png)
> Figure 6.2 Set up custom rules to trigger when browsing to the web yorku.ca (pt1)

![Screenshot 53](images/im53.png)
> Figure 6.3 Setting up custom rules to trigger when browsing to the web yorku.ca (pt2)

![Screenshot 54](images/im54.png)
> Figure 6.4 Got this with the command sudo cat /var/log/snort/alert_fast.txt after browsing to www.yorku.ca from Firefox; Unsuccessful with the trigger. 


### Conclusion:

Unsuccessful with the trigger as it doesn’t show anything on “Browsing yorku.ca found” as shown in figure 6.4. I tried `sudo` `grep` “Browsing yorku.ca found” `/var/log/``snort``/alert_fast.txt` command as troubleshoot and found no result. Also made sure my network card was on promiscuous mode by command `sudo` `ip link set` eth0 `promisc` on as an extra troubleshooting step still found no success in triggering the www.yorku.ca browser.