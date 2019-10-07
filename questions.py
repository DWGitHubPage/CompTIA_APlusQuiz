# Python 3.7.4

import random


class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer


question_prompts = [

  
"\nWhat is the port number of HTTP?\n"

"\n(a) 80\n"
"\n(b) 60\n"
"\n(c) 110\n"
"\n(d) 443\n" 
"\nAnswer: ",
"\n"

"What is the port number of POP3?\n"
"\n(a) 23\n"
"\n(b) 50\n"
"\n(c) 110\n"
"\n(d) 443\n" 
"\nAnswer: ",
"\n"

"How long is an eSATA cable?\n"

"\n(a) 12 inches\n"
"\n(b) 1 meter\n"
"\n(c) 2 meters\n"
"\n(d) 1 foot\n"
"\nAnswer: ",
"\n"

"A UEFI functionality designed to prevent the loading of malware & unauthorized\n" \
"OSs during system start-up is known as:\n"

"\n(a) LoJack\n"
"\n(b) Secure Boot\n"
"\n(c) Bitlocker\n"
"\n(d) Kerberos\n"
"\nAnswer: ",
"\n"

"Which of the following terms refers to a technology that allows for storing\n" \
"passwords, certificates, or encription keys in a hardware chip?\n" 

"\n(a) Access Control List(ACL)\n" 
"\n(b) Encrypting File System (EFS)\n"
"\n(c) User Account Control (UAC)\n"
"\n(d) Trusted Platform Module (TPM) \n"
"\nAnswer: ",
"\n"

"What is LoJack?\n"

"\n(a) Loopback adapter\n" 
"\n(b) Security feature used for locating stolen desktops, laptops, or tablets\n" 
"\n(c) Connector standard\n"
"\n(d) RJ-11 plug\n"
"\nAnswer: ",
"\n"
     
"Which type of password provides the highest level of permissions in BIOS?\n" 

"\n(a) root\n"
"\n(b) Supervisor\n"
"\n(c) Administrator\n"
"\n(d) Power User \n"
"\nAnswer: ",
"\n"

"Which of the protocols listed below is used for automated discovery of networked\n"
"services on Local Area Networks (LAN's)? \n"

"\n(a) SMB\n"
"\n(b) AFP\n"
"\n(c) CIFS\n"
"\n(d) SLP\n"
"\nAnswer: ",
"\n"

"Which of the protocols listed below was designed as a secure replacement for\n"
"Telnet?\n"

"\n(a) CHAP\n"
"\n(b) FTP\n"
"\n(c) SNMP\n"
"\n(d) SSH\n"
"\nAnswer: ",
"\n"

"Which of the following wireless encryption schemes offers the highest level\n"
"of protection?\n"

"\n(a) WEP\n"
"\n(b) WPA2\n"
"\n(c) WAP\n"
"\n(d) WPA\n"
"\nAnswer: ",
"\n"

"What is the most common motherboard type used in desktop PC's?\n"

"\n(a) ITX\n"
"\n(b) LPX\n"
"\n(c) ATX\n"
"\n(d) NLX\n"
"\nAnswer: ",
"\n"

"What is the port number of RDP (Remote Desktop Protocol)?\n"

"\n(a) 110\n"
"\n(b) 443\n"
"\n(c) 3389\n"
"\n(d) 67\n"
"\nAnswer: ",
"\n"

"Which of the answers listed below refers to a VIA-proprietary low-power\n"
"consumption SFF type motherboard known for industrial and embedded PC\n"
"applications?\n"

"\n(a) Mini-ITX\n"
"\n(b) LPX\n"
"\n(c) ATX\n"
"\n(d) NLX\n"
"\n(e) Mini-ATX\n"
"\nAnswer: ",
"\n"

"Peripheral Component Interconnect (PCI) is an example of a parallel\n"
"expansion bus (and a corresponding slot type) used for attaching hardware\n"
"devices (in the form of an integrated circuit or expansion card) to the\n"
"motherboard inside the computer case.\n"

"\n(a) True\n"
"\n(b) False\n"
"\nAnswer: ",
"\n"

"Which of the following correctly identifies the four possible entries in a\n"
"file allocation table?\n"

"\n(a) \n"
"\n(b) An end-of-file marker, a bad-block marker, code indicating the cluster\n"
"is available, the number of the cluster where the next part of the file is stored.\n"
"\n(c) Number of the starting cluster, number of the ending cluster, number\n"
"of used clusters, number of available clusters.\n"
"\n(d) Filename, date, time, size.\n"
"\nAnswer: ",
"\n"

"In PCIe architecture, a single full-duplex point-to-point serial\n"
"communication path consisting of two pairs of wires (where one pair\n"
"is used for transmitting data and the other pair for receiving data)\n"
"is known as:\n"

"\n(a) Lane\n"
"\n(b) Dual channel\n"
"\n(c) Dual rail\n"
"\n(d) Duplexing assembly\n"
"\nAnswer: ",
"\n"

"Which of the following integrated circuit types defines the core\n"
"functionality and capabilities of a motherboard?\n"

"\n(a) Northbridge\n"
"\n(b) Southbridge\n"
"\n(c) I/O Controller Hub (ICH)\n"
"\n(d) Fusion Controller Hub (FCH)\n"
"\n(e) Chipset\n"
"\nAnswer: ",
"\n"

"ExpressCards connect to which two buses?\n"

"\n(a) USB and PCIe's\n"
"\n(b) ACPI and PCI's\n"
"\n(c) USB and PCI's\n"
"\n(d) PCIe and ACPI's\n"
"\nAnswer: ",
"\n"

"Which of the following display types will you commonly find on a\n"
"portable PC today?\n"

"\n(a) OLED\n"
"\n(b) Plasma\n"
"\n(c) CRT\n"
"\n(d) LCD\n"
"\nAnswer: ",
"\n"

"What type of battery do manufacturers use today for portables?\n"

"\n(a) Nickel-Cadmium (Ni-Cd)\n"
"\n(b) Lithium-Ion (Li-Ion)\n"
"\n(c) Nickel-Metal Hydride (Ni-MH)\n"
"\n(d) Nickel-Lithium (Ni-Li)\n"
"\nAnswer: ",
"\n"

"Which two width's do ExpressCards come in?\n"

"\n(a) 24-mm and 54-mm\n"
"\n(b) 36-mm and 52-mm\n"
"\n(c) 48-mm and 56-mm\n"
"\n(d) 34-mm and 54-mm\n"
"\nAnswer: ",
"\n"

"Powerful hypervisors like ESXi are often booted from?\n"

"\n(a) USB thumbdrives\n"
"\n(b) Floppy Disks\n"
"\n(c) Windows\n"
"\n(d) Firmware\n"
"\nAnswer: ",
"\n"

"Which two features lets you save a VM's state so you can quickly restore\n"
"to that point?\n"

"\n(a) Save and Snapshot\n"
"\n(b) Save and Zip\n"
"\n(c) Checkpoint and Snapshot\n"
"\n(d) Checkshot and Snappoint\n"
"\nAnswer: ",
"\n"

"Which mobile OS enables developers to customize the user experience\n"
"without restrictions\n?"

"\n(a) Blackberry\n"
"\n(b) Android\n"
"\n(c) Windows Phone\n"
"\n(d) iOS\n"
"\nAnswer: ",
"\n"

"Which mobile device screen technology uses no backlight?\n"

"\n(a) BYOD\n"
"\n(b) LCD\n"
"\n(c) LED\n"
"\n(d) OLED\n"
"\nAnswer: ",
"\n"

"Using your stored credit card information on your smartphone used which\n"
"technology to make the transaction?\n"

"\n(a) Wi-Fi calling\n"
"\n(b) NFC (Near Field Communication)\n"
"\n(c) BitLocker To Go\n"
"\n(d) Swipe lock\n"
"\nAnswer: ",
"\n"

"Which of the following is a 15-digit number used to uniquly identify\n"
"a mobile device that connects to a cellular network?\n"

"\n(a) IMSI\n"
"\n(b) ICCID\n"
"\n(c) GSM\n"
"\n(d) IMEI\n"
"\nAnswer: ",
"\n"

"Which mobile operating system requires a third-party software firewall?\n"

"\n(a) Windows Mobile\n"
"\n(b) iOS\n"
"\n(c) Android\n"
"\n(d) macOS\n"
"\nAnswer: ",
"\n"

"What do app scanners do?\n"
"\n(a) Scan QR codes for hidden codes\n"
"\n(b) Analzye Wi-Fi signals to identify evil-twin WAP's\n"
"\n(c) Analyze the traffic into & out of an application for\n"
"suspicious behavior\n"
"\n(d) Analyze the permissions used by installed applications to\n"
"highlight security risks\n"
"\nAnswer: ",
"\n"

"Best way to protect data on a removable media card?\n"
"\n(a) Format it\n"
"\n(b) Lock it\n"
"\n(c) Encrypt it\n"
"\n(d) Remove it when needed\n"
"\nAnswer: ",
"\n"

"Jailbreaking an iPhone gives access to?\n"
"\n(a) The /bin folder\n"
"\n(b) The system BIOS\n"
"\n(c) The root account\n"
"\n(d) The administrator account\n"
"\n(e) The user account\n"
"\nAnswer: ",
"\n"


"What mechanism is used by most inkjet printers to push ink ont\n"
"the printer?\n"

"\n(a) Print spool\n"
"\n(b) Electrostatic discharge\n"
"\n(c) Electroconductive plates\n"
"\n(d) Printwires\n"
"\nAnswer: ",
"\n"


"With a laser printer, what creates the image on the photosensitive\n"
"drum?\n"

"\n(a) Toner\n"
"\n(b) Primary corona\n"
"\n(c) Transfer corona\n"
"\n(d) Laser imaging unit\n"
"\nAnswer: ",
"\n"


"The printer prints a test page with no problem, but it makes a mess\n"
"when trying to print multiple pages. What's most likely the problem?\n"

"\n(a) Faulty software configuration\n"
"\n(b) Out of toner\n"
"\n(c) Printer interface\n"
"\n(d) Fuser error\n"
"\nAnswer: ",
"\n"

"Which tool would help you determine why a print job didn't print?\n"

"\n(a) System setup\n"
"\n(b) Print spooler\n"
"\n(c) Printer driver\n"
"\n(d) Printer setup\n"
"\nAnswer: ",
"\n"

"Which of the following might offer good hardware authentication?\n"

"\n(a) Smart cards\n"
"\n(b) NTFS\n"
"\n(c) Encrypted passwords\n"
"\n(d) Strong passwords\n"
"\nAnswer: ",
"\n"

"Which hardware firewall feature enables incoming traffic on a specific\n"
"port to reach an IP address on the LAN?\n"

"\n(a) DMZ\n"
"\n(b) Trigger port\n"
"\n(c) Multifactor authentication\n"
"\n(d) Port forwarding\n"
"\nAnswer: ",
"\n"

"Which of these choices would provide better security on a Wi-Fi router?\n"

"\n(a) WPA2\n"
"\n(b) WPA\n"
"\n(c) WAP\n"
"\n(d) SecureDNS\n"
"\nAnswer: ",
"\n"

"\n"
"\n(a) \n"
"\n(b) \n"
"\n(c) \n"
"\n(d) \n"
"\nAnswer: ",
"\n"

"What broad term describes the process of creating a road map for current\n"
"& future techs to make changes or repairs over time for an organization?\n"

"\n(a) Network documentation\n"
"\n(b) Management documentation\n"
"\n(c) Change management\n"
"\n(d) Change documentation\n"
"\nAnswer: ",
"\n"

"What broad term describes the process of enabling organizations to\n"
"implement changes to IT infrastructure in a safe & cost-effective manner?\n"

"\n(a) Management documentation\n"
"\n(b) Change documentation\n"
"\n(c) Network documentation\n"
"\n(d) Change management\n"
"\nAnswer: ",
"\n"

"Which device protects computing devices from blackout & power dips?\n"

"\n(a) GPS\n"
"\n(b) Surge suppressor\n"
"\n(c) UPS (Uninterruptible Power Supply)\n"
"\n(d) Surge protector\n"
"\nAnswer: ",
"\n"

"Which Microsoft Windows OS utility can be used to view basic information\n"
"about computer's BIOS?\n"

"\n(a) SERVICES.MSC\n"
"\n(b) Control Panel\n"
"\n(c) WINVER.EXE\n"
"\n(d) MISINFO32.EXE\n"
"\nAnswer: ",
"\n"

"Power failure during BIOS upgrade can be the cause of irreversible\n"
"damage to the computer system.\n"

"\n(a) True\n"
"\n(b) False\n"
"\nAnswer: ",
"\n"

"After a normal system shutdown, when the computer is turned off, contents\n"
"of the memory used to store BIOS settings are:\n"

"\n(a) Retained\n"
"\n(b) Erased\n"
"\n(c) Stored in a page file\n"
"\n(d) Saved on a hard drive\n"
"\nAnswer: ",
"\n"

"Which of the acronyms listed refers to a series of basic hardware\n"
"diagnostic tests performed by the startup BIOS after the computer is\n"
"powered on?\n"

"\n(a) POTS\n"
"\n(b) POST\n"
"\n(c) Qos\n"
"\n(d) IDE\n"
"\nAnswer: ",
"\n"

"After replacing a modular hardware component inside a computer case, the\n"
"updated information about specific parameters of the new device can be?\n"


"\n(a) Secondary storage and System BIOS\n"
"\n(b) System BIOS and Flash memory\n"
"\n(c) CMOS RAM and ROM\n"
"\n(d) Flash memory and CMOS RAM\n"
"\nAnswer: ",
"\n"

"In order to work, an integrated component such as Network Interface Card\n"
"(NIC) on a newly assembled computer system may need to be first:\n"

"\n(a) Checked against the Hardware Compatibility List (HCL)\n"
"\n(b) Enabled in the advanced BIOS settings menu\n"
"\n(c) Enabled in Windows Control Panel\n"
"\n(d) Updated with the latest driver in Device Manager\n"
"\nAnswer: ",
"\n"

"Which of the following answers to a firmware interface designed as a\n"
"replacement for BIOS?\n"

"\n(a) USMT\n"
"\n(b) ACPI\n"
"\n(c) UEFI\n"
"\n(d) CMOS\n"
"\nAnswer: ",
"\n"

"Which of the following statements is true?\n"

"\n(a) A common security measure is to store BIOS on a non-rewritable\n"
"memory chip.\n"
"\n(b) The process of BIOS update can be aborted & resumed later.\n"
"\n(c) Aborted BIOS update could render the computer unusable.\n"
"\n(d) Aborted BIOS update can be resumed by the transaction recovery system.\n"
"\nAnswer: ",
"\n"

"Which of the following terms refers to a technology that allows for storing\n"
"passwords, certificates, or encryption keys in a hardware chip?\n"

"\n(a) User Account Control (UAC)\n"
"\n(b) Access Control List (ACL)\n"
"\n(c) Encrypting File System\n"
"\n(d) Trusted Platform Module (TPM)\n"
"\nAnswer: ",
"\n"

"A UEFI functionality designed to prevent the loading of malware &\n"
"unauthorized OS's during system start-up is known as:\n"

"\n(a) Bitlocker\n"
"\n(b) Kerberos\n"
"\n(c) Secure boot\n"
"\n(d) LoJack\n"
"\nAnswer: ",
"\n"

"What is the port number of DNS (Domain Name System?\n"

"\n(a) 60\n"
"\n(b) 53\n"
"\n(c) 45\n"
"\n(d) 62\n"
"\nAnswer: ",
"\n"

"What is the number of contact pins used in SDR SDRAM modules?\n"

"\n(a) 184\n"
"\n(b) 240\n"
"\n(c) 144\n"
"\n(d) 168\n"
"\nAnswer: ",
"\n"

"A single Data Rate Synchronous Dynamic Random Access Memory (SDR SDRAM)\n"
"can read/write one word of data per clock cycle.\n"

"\n(a) True\n"
"\n(b) False\n"
"\nAnswer: ",
"\n"

"Which of the memory types listed below are designed to store permanent data\n"
"that cannot be changed?\n"

"\n(a) PROM and EEPROM\n"
"\n(b) ROM and RAM\n"
"\n(c) ROM and PROM\n"
"\n(d) EPROM and EEPROM\n"
"\nAnswer: ",
"\n"

"What is the name of the most common connector type used for providing power\n"
"to various hardware components inside the computer case?\n"

"\n(a) Molex\n"
"\n(b) RJ-45\n"
"\n(c) USB\n"
"\n(d) BNC\n"
"\nAnswer: ",
"\n"

"Which of the answers listed below refers to the industry name used for\n"
"DDR3-1333 modules?\n"

"\n(a) PC3-6400\n"
"\n(b) PC3-12800\n"
"\n(c) PC3-8500\n"
"\n(d) PC3-10600\n"
"\nAnswer: ",
"\n"

"What is the maximum amount of data that can be transferred each second by a\n"
"DDR3-1600 module?\n"

"\n(a) 12800 MB/s\n"
"\n(b) 8533 MB/s\n"
"\n(c) 10667 MB/s\n"
"\n(d) 6400 MB/s\n"
"\nAnswer: ",
"\n"

"What is the most common memory module form factor type used in laptop\n"
"computers?\n"

"\n(a) C-RIMM\n"
"\n(b) SO-DIMM\n"
"\n(c) MicroDIMM\n"
"\n(d) DIMM\n"
"\nAnswer: ",
"\n"

"What is the maximum amount of bytes that a 32-bit system can address?\n"

"\n(a) 32 GB\n"
"\n(b) 4 GB\n"
"\n(c) 12 GB\n"
"\n(d) 2 GB\n"
"\nAnswer: ",
"\n"

"How much memory can a 64-bit register theoretically reference?\n"

"\n(a) 16 GB\n"
"\n(b) 64 GB\n"
"\n(c) 2 EB\n"
"\n(d) 16 EB\n"
"\nAnswer: ",
"\n"

"What is a KVM (Keyboard, Video, Mouse) switch?\n"

"\n(a) A USB connector for a keyboard, video monitor, or mouse.\n"
"\n(b) A switch to turn on/off a keyboard, video, or mouse.\n"
"\n(c) A hardware device that allows a user to control multiple computers\n"
"from one or more sets of keyboards, video monitors, & mice.\n"
"\n(d) An extra smart card for a keyboard, video monitor, or mouse.\n"
"\nAnswer: ",
"\n"

"Which of the following port numbers are reserved for NetBIOS services?\n"

"\n(a) 137, 138, 139\n"
"\n(b) 136, 137, 138, 139\n"
"\n(c) 134, 135, 136\n"
"\n(d) 20, 21, 23, 25\n"
"\nAnswer: ",
"\n"

"Which of the port numbers listed below is used by an Apple-proprietary\n"
"file sharing protocol?\n"

"\n(a) 445\n"
"\n(b) 548\n"
"\n(c) 443\n"
"\n(d) 110\n"
"\nAnswer: ",
"\n"

"What is the function of POP3?\n"

"\n(a) Sending email messages\n"
"\n(b) File Exchange\n"
"\n(c) Retrieving email messages from a mail server\n"
"\n(d) Sending and Retrieving email messages from a mail server\n"
"\nAnswer: ",
"\n"

"IMAP4 is used for?\n"

"\n(a) Retrieving email messages from a mail server\n"
"\n(b) Sending email messages\n"
"\n(c) Sending and retrieving email messages\n"
"\n(d) Sending email messages with encryption\n"
"\nAnswer: ",
"\n"

"What program does Microsoft include with Windows to partition & format a drive?\n"

"\n(a) Disk Management console\n"
"\n(b) Format\n"
"\n(c) System Commander\n"
"\n(d) Disk Administrator console\n"
"\nAnswer: ",
"\n"

"Which storage option in Windows 8 or later offers the best mix of resiliency &\n"
"performance with two drives?\n"

"\n(a) Simple space\n"
"\n(b) Parity space\n"
"\n(c) Three-way mirror space\n"
"\n(d) Two-way mirror space\n"
"\nAnswer: ",
"\n"

"Which configuration requires three same-sized volumes?\n"

"\n(a) RAID 0\n"
"\n(b) Striped volume\n"
"\n(c) RAID 5\n"
"\n(d) Spanned volume\n"
"\nAnswer: ",
"\n"

"How much data can a dvd hold?\n"

"\n(a) 2 GB\n"
"\n(b) 4.7 GB\n"
"\n(c) 16 GB\n"
"\n(d) 500 MB\n"
"\nAnswer: ",
"\n"

]


questions = [
     Question(question_prompts[0], 'a'),
     Question(question_prompts[1], 'c'),
     Question(question_prompts[2], 'c'),
     Question(question_prompts[3], 'b'),
     Question(question_prompts[4], 'd'),
     Question(question_prompts[5], 'b'),
     Question(question_prompts[6], 'b'),
     Question(question_prompts[7], 'd'),
     Question(question_prompts[8], 'd'),
     Question(question_prompts[9], 'b'),
     Question(question_prompts[10], 'a'),
     Question(question_prompts[11], 'c'),
     Question(question_prompts[12], 'a'),
     Question(question_prompts[13], 'a'),
     Question(question_prompts[14], 'b'),
     Question(question_prompts[15], 'a'),
     Question(question_prompts[16], 'e'),
     Question(question_prompts[17], 'a'),
     Question(question_prompts[18], 'd'),
     Question(question_prompts[19], 'b'),
     Question(question_prompts[20], 'd'),
     Question(question_prompts[21], 'a'),
     Question(question_prompts[22], 'c'),
     Question(question_prompts[23], 'b'),
     Question(question_prompts[24], 'd'),
     Question(question_prompts[25], 'b'),
     Question(question_prompts[26], 'd'),
     Question(question_prompts[27], 'c'),
     Question(question_prompts[28], 'd'),
     Question(question_prompts[29], 'c'),
     Question(question_prompts[30], 'c'),
     Question(question_prompts[31], 'c'),
     Question(question_prompts[32], 'd'),
     Question(question_prompts[33], 'a'),
     Question(question_prompts[34], 'b'),
     Question(question_prompts[35], 'a'),
     Question(question_prompts[36], 'd'),
     Question(question_prompts[37], 'a'),
     Question(question_prompts[38], 'a'),
     Question(question_prompts[39], 'd'),
     Question(question_prompts[40], 'c'),
     Question(question_prompts[41], 'd'),
     Question(question_prompts[42], 'a'),
     Question(question_prompts[43], 'a'),
     Question(question_prompts[44], 'b'),
     Question(question_prompts[45], 'd'),
     Question(question_prompts[46], 'b'),
     Question(question_prompts[47], 'c'),
     Question(question_prompts[48], 'c'),
     Question(question_prompts[49], 'd'),
     Question(question_prompts[50], 'c'),
     Question(question_prompts[51], 'b'),
     Question(question_prompts[52], 'd'),
     Question(question_prompts[53], 'a'),
     Question(question_prompts[54], 'c'),
     Question(question_prompts[55], 'a'),
     Question(question_prompts[56], 'd'),
     Question(question_prompts[57], 'a'),
     Question(question_prompts[58], 'a'),
     Question(question_prompts[59], 'b'),
     Question(question_prompts[60], 'd'),
     Question(question_prompts[61], 'c'),
     Question(question_prompts[62], 'a'),
     Question(question_prompts[63], 'b'),
     Question(question_prompts[64], 'c'),
     Question(question_prompts[65], 'a'),
     Question(question_prompts[66], 'a'),
     Question(question_prompts[67], 'd'),
     Question(question_prompts[68], 'c'),
     Question(question_prompts[69], 'b'),
]


