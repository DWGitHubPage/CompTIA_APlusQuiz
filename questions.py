# Python 3.7.4

import random


class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer


question_prompts = [

# 0.  
'''What is the port number of HTTP?

(a) 80.

(b) 60.

(c) 110.

(d) 443.

Answer: ''',
"\n"

     
# 1.
'''What is the port number of POP3?

(a) 23.

(b) 50.

(c) 110.

(d) 443.

Answer: ''',
'\n'

     
# 2.
'''How long is an eSATA cable?

(a) 12 inches.

(b) 1 meter.

(c) 2 meters.

(d) 1 foot.

Answer: ''',
'\n'


# 3.     
'''A UEFI functionality designed to prevent the loading of malware & unauthorized
OSs during system start-up is known as:

(a) LoJack.

(b) Secure Boot.

(c) Bitlocker.

(d) Kerberos.

Answer: ''',
'\n'


# 4.
'''Which of the following terms refers to a technology that allows for storing
passwords, certificates, or encription keys in a hardware chip?

(a) Access Control List (ACL).

(b) Encrypting File System (EFS).

(c) User Account Control (UAC).

(d) Trusted Platform Module (TPM).

Answer: ''',
'\n'

     
# 5.
'''What is LoJack?

(a) Loopback adapter. 

(b) Security feature used for locating stolen desktops, laptops, or tablets.

(c) Connector standard.

(d) RJ-11 plug.

Answer: ''',
'\n'
  
     
# 6. 
'''Which type of password provides the highest level of permissions in BIOS?

(a) Root.

(b) Supervisor.

(c) Administrator.

(d) Power User.

Answer: ''',
'\n'

     
# 7.     
'''Which of the protocols listed below is used for automated discovery of networked
services on Local Area Networks (LAN's)?

(a) SMB.

(b) AFP.

(c) CIFS.

(d) SLP.

Answer: ''',
'\n'

     
# 8.     
'''Which of the protocols listed below was designed as a secure replacement for
Telnet?

(a) CHAP.

(b) FTP.

(c) SNMP.

(d) SSH.

Answer: ''',
'\n'

     
# 9.     
'''Which of the following wireless encryption schemes offers the highest level
of protection?

(a) WEP.

(b) WPA2.

(c) WAP.

(d) WPA.

Answer: ''',
'\n'

     
# 10     
'''What is the most common motherboard type used in desktop PC's?

(a) ITX.

(b) LPX.

(c) ATX.

(d) NLX.

Answer: ''',
'\n'

     
# 11.     
'''What is the port number of RDP (Remote Desktop Protocol)?

(a) 110.

(b) 443.

(c) 3389.

(d) 67.

Answer: ''',
'\n'

     
# 12     
'''Which of the answers listed below refers to a VIA-proprietary low-power
consumption SFF type motherboard known for industrial and embedded PC
applications?

(a) Mini-ITX.

(b) LPX.

(c) ATX.

(d) NLX.

(e) Mini-ATX.

Answer: ''',
'\n'

     
# 13.     
'''Peripheral Component Interconnect (PCI) is an example of a parallel
expansion bus (and a corresponding slot type) used for attaching hardware
devices (in the form of an integrated circuit or expansion card) to the
motherboard inside the computer case.

(a) True.

(b) False.

Answer: ''',
'\n'

     
# 14.     
'''Which of the following correctly identifies the four possible entries in a
file allocation table?

(a) Filename, start of cluster, end of cluster, date.

(b) An end-of-file marker, a bad-block marker, code indicating the cluster
is available, the number of the cluster where the next part of the file is stored.

(c) Number of the starting cluster, number of the ending cluster, number of used 
clusters, number of available clusters.

(d) Filename, date, time, size.

Answer: ''',
'\n'

     
# 15.     
'''In PCIe architecture, a single full-duplex point-to-point serial communication 
path consisting of two pairs of wires (where one pair is used for transmitting 
data and the other pair for receiving data) is known as:

(a) Lane.

(b) Dual channel.

(c) Dual rail.

(d) Duplexing assembly.

Answer: ''',
'\n'

     
# 16.     
'''Which of the following integrated circuit types defines the core functionality 
and capabilities of a motherboard?

(a) Northbridge.

(b) Southbridge.

(c) I/O Controller Hub (ICH).

(d) Fusion Controller Hub (FCH).

(e) Chipset.

Answer: ''',
'\n'

     
# 17.     
'''ExpressCards connect to which two buses?

(a) USB and PCIe's.

(b) ACPI and PCI's.

(c) USB and PCI's.

(d) PCIe and ACPI's.

Answer: ''',
'\n'

     
# 18.     
'''Which of the following display types will you commonly find on a portable 
PC today?

(a) OLED.

(b) Plasma.

(c) CRT.

(d) LCD.

Answer: ''',
'\n'

     
# 19.     
'''What type of battery do manufacturers use today for portables?

(a) Nickel-Cadmium (Ni-Cd).

(b) Lithium-Ion (Li-Ion).

(c) Nickel-Metal Hydride (Ni-MH).

(d) Nickel-Lithium (Ni-Li).

Answer: ''',
'\n'

     
# 20.     
'''Which two width's do ExpressCards come in?

(a) 24-mm and 54-mm.

(b) 36-mm and 52-mm.

(c) 48-mm and 56-mm.

(d) 34-mm and 54-mm.

Answer: ''',
'\n'

     
# 21.     
'''Powerful hypervisors like ESXi are often booted from?

(a) USB thumbdrives.

(b) Floppy Disks.

(c) Windows.

(d) Firmware.

Answer: ''',
'\n'

     
# 22.     
'''Which two features lets you save a VM's state so you can quickly restore
to that point?

(a) Save and Snapshot.

(b) Save and Zip.

(c) Checkpoint and Snapshot.

(d) Checkshot and Snappoint.

Answer: ''',
'\n'

     
# 23.     
'''Which mobile OS enables developers to customize the user experience
"without restrictions?

(a) Blackberry.

(b) Android.

(c) Windows Phone.

(d) iOS.

Answer: ''',
'\n'

     
# 24.
'''Which mobile device screen technology uses no backlight?

(a) BYOD.

(b) LCD.

(c) LED.

(d) OLED.

Answer: ''',
'\n'

     
# 25.     
'''Using your stored credit card information on your smartphone used which technology 
to make the transaction?

(a) Wi-Fi calling.

(b) NFC (Near Field Communication).

(c) BitLocker To Go.

(d) Swipe lock.

Answer: ''',
'\n'

     
# 26.     
'''Which of the following is a 15-digit number used to uniquly identify a mobile 
device that connects to a cellular network?

(a) IMSI.

(b) ICCID.

(c) GSM.

(d) IMEI.

Answer: ''',
'\n'

     
# 27.     
'''Which mobile operating system requires a third-party software firewall?

(a) Windows Mobile.

(b) iOS.

(c) Android.

(d) macOS.

Answer: ''',
'\n'

     
# 28.     
'''What do app scanners do?

(a) Scan QR codes for hidden codes.

(b) Analzye Wi-Fi signals to identify evil-twin WAP's.

(c) Analyze the traffic into & out of an application for
suspicious behavior.

(d) Analyze the permissions used by installed applications to highlight 
security risks.

Answer: ''',
'\n'

     
# 29.
'''Best way to protect data on a removable media card?

(a) Format it.

(b) Lock it.

(c) Encrypt it.

(d) Remove it when needed.

Answer: ''',
'\n'

     
# 30.     
'''Jailbreaking an iPhone gives access to?

(a) The /bin folder.

(b) The system BIOS.

(c) The root account.

(d) The administrator account.

(e) The user account.

Answer: ''',
'\n'

     
# 31.
'''What mechanism is used by most inkjet printers to push ink onto
"the printer?

(a) Print spool.

(b) Electrostatic discharge.

(c) Electroconductive plates.

(d) Printwires.

Answer: ''',
'\n'


# 32.     
'''With a laser printer, what creates the image on the photosensitive
"drum?

(a) Toner.

(b) Primary corona.

(c) Transfer corona.

(d) Laser imaging unit.

Answer: ''',
'\n'

     
# 33.
'''The printer prints a test page with no problem, but it makes a mess
when trying to print multiple pages. What's most likely the problem?

(a) Faulty software configuration.

(b) Out of toner.

(c) Printer interface.

(d) Fuser error.

Answer: ''',
'\n'

     
# 34.     
'''Which tool would help you determine why a print job didn't print?

(a) System setup.

(b) Print spooler.

(c) Printer driver.

(d) Printer setup.

Answer: ''',
'\n'

     
# 35.     
'''Which of the following might offer good hardware authentication?

(a) Smart cards.

(b) NTFS.

(c) Encrypted passwords.

(d) Strong passwords.

Answer: ''',
'\n'

     
# 36.     
'''Which hardware firewall feature enables incoming traffic on a specific
port to reach an IP address on the LAN?

(a) DMZ.

(b) Trigger port.

(c) Multifactor authentication.

(d) Port forwarding.

Answer: ''',
"'\n'

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


