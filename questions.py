# Python 3.7.4

import random


class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer


qn_prompt = [

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
'\n'

# 37.     
'''Which of these choices would provide better security on a Wi-Fi router?

(a) WPA2.

(b) WPA.

(c) WAP.

(d) SecureDNS.

Answer: ''',
'\n'

# 38.
'''What broad term describes the process of creating a road map for current
& future techs to make changes or repairs over time for an organization?

(a) Network documentation.

(b) Management documentation.

(c) Change management.

(d) Change documentation.

Answer: ''',
'\n'

# 39.     
'''What broad term describes the process of enabling organizations to
implement changes to IT infrastructure in a safe & cost-effective manner?

(a) Management documentation.

(b) Change documentation.

(c) Network documentation.

(d) Change management.

Answer: ''',
'\n'

# 40.     
'''Which device protects computing devices from blackout & power dips?

(a) GPS.

(b) Surge suppressor.

(c) UPS (Uninterruptible Power Supply).

(d) Surge protector.

Answer: ''',
'\n'

# 41.     
'''Which Microsoft Windows OS utility can be used to view basic information
about computer's BIOS?

(a) SERVICES.MSC.

(b) Control Panel.

(c) WINVER.EXE.

(d) MISINFO32.EXE.

Answer: ''',
'\n'

# 42.     
'''Power failure during BIOS upgrade can be the cause of irreversible damage 
to the computer system.

(a) True.

(b) False.

Answer: ''',
'\n'

# 43.     
'''After a normal system shutdown, when the computer is turned off, contents of 
the memory used to store BIOS settings are:

(a) Retained.

(b) Erased.

(c) Stored in a page file.

(d) Saved on a hard drive.

Answer: ''',
'\n'

# 44.     
'''Which of the acronyms listed refers to a series of basic hardware diagnostic 
tests performed by the startup BIOS after the computer is powered on?\n"

(a) POTS.

(b) POST.

(c) QoS.

(d) IDE.

Answer: ''',
'\n'

# 45.     
'''After replacing a modular hardware component inside a computer case, the
updated information about specific parameters of the new device can be?

(a) Secondary storage and System BIOS.

(b) System BIOS and Flash memory.

(c) CMOS RAM and ROM.

(d) Flash memory and CMOS RAM.

Answer: ''',
'\n'

# 46.     
'''In order to work, an integrated component such as Network Interface Card (NIC) 
on a newly assembled computer system may need to be first:

(a) Checked against the Hardware Compatibility List (HCL).

(b) Enabled in the advanced BIOS settings menu.

(c) Enabled in Windows Control Panel.

(d) Updated with the latest driver in Device Manager.

Answer: ''',
'\n'

# 47.     
'''Which of the following answers to a firmware interface designed as a replacement 
for BIOS?

(a) USMT.

(b) ACPI.

(c) UEFI.

(d) CMOS.

Answer: ''',
'\n'

# 48.     
'''Which of the following statements is true?

(a) A common security measure is to store BIOS on a non-rewritable memory chip.

(b) The process of BIOS update can be aborted & resumed later.

(c) Aborted BIOS update could render the computer unusable.

(d) Aborted BIOS update can be resumed by the transaction recovery system.

Answer: ''',
'\n'

# 49.     
'''Which of the following terms refers to a technology that allows for storing
passwords, certificates, or encryption keys in a hardware chip?

(a) User Account Control (UAC).

(b) Access Control List (ACL).

(c) Encrypting File System.

(d) Trusted Platform Module (TPM).

Answer: ''',
'\n'

# 50.     
'''A UEFI functionality designed to prevent the loading of malware &
unauthorized OS's during system start-up is known as:

(a) Bitlocker.

(b) Kerberos.

(c) Secure boot.

(d) LoJack.

Answer: ''',
'\n'

# 51.     
'''What is the port number of DNS (Domain Name System?

(a) 60.

(b) 53.

(c) 45.

(d) 62.

Answer: ''',
'\n'

# 52.     
'''What is the number of contact pins used in SDR SDRAM modules?

(a) 184.

(b) 240.

(c) 144.

(d) 168.

Answer: ''',
'\n'

# 53.     
'''A single Data Rate Synchronous Dynamic Random Access Memory (SDR SDRAM)
can read/write one word of data per clock cycle.

(a) True.

(b) False.

Answer: ''',
'\n'

# 54.     
'''Which of the memory types listed below are designed to store permanent data
that cannot be changed?

(a) PROM and EEPROM.

(b) ROM and RAM.

(c) ROM and PROM.

(d) EPROM and EEPROM.

Answer: ''',
'\n'

# 55.     
'''What is the name of the most common connector type used for providing power to 
various hardware components inside the computer case?

(a) Molex.

(b) RJ-45.

(c) USB.

(d) BNC.

Answer: ''',
'\n'

# 56.     
'''Which of the answers listed below refers to the industry name used for
DDR3-1333 modules?

(a) PC3-6400.

(b) PC3-12800.

(c) PC3-8500.

(d) PC3-10600.

Answer: ''',
'\n'

# 57.     
'''What is the maximum amount of data that can be transferred each second by a
DDR3-1600 module?

(a) 12800 MB's.

(b) 8533 MB's.

(c) 10667 MB's.

(d) 6400 MB's.

Answer: ''',
'\n'

# 58.     
'''What is the most common memory module form factor type used in laptop computers?

(a) C-RIMM.

(b) SO-DIMM.

(c) MicroDIMM.

(d) DIMM.

Answer: ''',
'\n'

# 59.     
'''What is the maximum amount of bytes that a 32-bit system can address?

(a) 32 GB.

(b) 4 GB.

(c) 12 GB.

(d) 2 GB.

Answer: ''',
'\n'

# 60.     
'''How much memory can a 64-bit register theoretically reference?

(a) 16 GB.

(b) 64 GB.

(c) 2 EB.

(d) 16 EB.

Answer: ''',
'\n'

# 61.     
'''What is a KVM (Keyboard, Video, Mouse) switch?

(a) A USB connector for a keyboard, video monitor, or mouse.

(b) A switch to turn on/off a keyboard, video, or mouse.

(c) A hardware device that allows a user to control multiple computers from 
one or more sets of keyboards, video monitors, & mice.

(d) An extra smart card for a keyboard, video monitor, or mouse.

Answer: ''',
'\n'

# 62.     
'''Which of the following port numbers are reserved for NetBIOS services?

(a) 137, 138, 139.

(b) 136, 137, 138, 139.

(c) 134, 135, 136.

(d) 20, 21, 23, 25.

Answer: ''',
'\n'

# 63.     
'''Which of the port numbers listed below is used by an Apple-proprietary
file sharing protocol?

(a) 445.

(b) 548.

(c) 443.

(d) 110.

Answer: ''',
'\n'

# 64.     
'''What is the function of POP3?

(a) Sending email messages.

(b) File Exchange.

(c) Retrieving email messages from a mail server.

(d) Sending and Retrieving email messages from a mail server.

Answer: ''',
'\n'

# 65.     
'''IMAP4 is used for?

(a) Retrieving email messages from a mail server.

(b) Sending email messages.

(c) Sending and retrieving email messages.

(d) Sending email messages with encryption.

Answer: ''',
'\n'

# 66.     
'''What program does Microsoft include with Windows to partition & format a drive?

(a) Disk Management console.

(b) Format.

(c) System Commander.

(d) Disk Administrator console.

Answer: ''',
'\n'

# 67.     
'''Which storage option in Windows 8 or later offers the best mix of resiliency &
performance with two drives?

(a) Simple space.

(b) Parity space.

(c) Three-way mirror space.

(d) Two-way mirror space.

Answer: ''',
'\n'

# 68.     
'''Which configuration requires three same-sized volumes?

(a) RAID 0.

(b) Striped volume.

(c) RAID 5.

(d) Spanned volume.

Answer: ''',
'\n'

# 69.     
'''How much data can a dvd hold?

(a) 2 GB.

(b) 4.7 GB.

(c) 16 GB.

(d) 500 MB.

Answer: ''',
'\n'

]

questions = [
     Question(qn_prompt[0], 'a'),
     Question(qn_prompt[1], 'c'),
     Question(qn_prompt[2], 'c'),
     Question(qn_prompt[3], 'b'),
     Question(qn_prompt[4], 'd'),
     Question(qn_prompt[5], 'b'),
     Question(qn_prompt[6], 'b'),
     Question(qn_prompt[7], 'd'),
     Question(qn_prompt[8], 'd'),
     Question(qn_prompt[9], 'b'),
     Question(qn_prompt[10], 'a'),
     Question(qn_prompt[11], 'c'),
     Question(qn_prompt[12], 'a'),
     Question(qn_prompt[13], 'a'),
     Question(qn_prompt[14], 'b'),
     Question(qn_prompt[15], 'a'),
     Question(qn_prompt[16], 'e'),
     Question(qn_prompt[17], 'a'),
     Question(qn_prompt[18], 'd'),
     Question(qn_prompt[19], 'b'),
     Question(qn_prompt[20], 'd'),
     Question(qn_prompt[21], 'a'),
     Question(qn_prompt[22], 'c'),
     Question(qn_prompt[23], 'b'),
     Question(qn_prompt[24], 'd'),
     Question(qn_prompt[25], 'b'),
     Question(qn_prompt[26], 'd'),
     Question(qn_prompt[27], 'c'),
     Question(qn_prompt[28], 'd'),
     Question(qn_prompt[29], 'c'),
     Question(qn_prompt[30], 'c'),
     Question(qn_prompt[31], 'c'),
     Question(qn_prompt[32], 'd'),
     Question(qn_prompt[33], 'a'),
     Question(qn_prompt[34], 'b'),
     Question(qn_prompt[35], 'a'),
     Question(qn_prompt[36], 'd'),
     Question(qn_prompt[37], 'a'),
     Question(qn_prompt[38], 'a'),
     Question(qn_prompt[39], 'd'),
     Question(qn_prompt[40], 'c'),
     Question(qn_prompt[41], 'd'),
     Question(qn_prompt[42], 'a'),
     Question(qn_prompt[43], 'a'),
     Question(qn_prompt[44], 'b'),
     Question(qn_prompt[45], 'd'),
     Question(qn_prompt[46], 'b'),
     Question(qn_prompt[47], 'c'),
     Question(qn_prompt[48], 'c'),
     Question(qn_prompt[49], 'd'),
     Question(qn_prompt[50], 'c'),
     Question(qn_prompt[51], 'b'),
     Question(qn_prompt[52], 'd'),
     Question(qn_prompt[53], 'a'),
     Question(qn_prompt[54], 'c'),
     Question(qn_prompt[55], 'a'),
     Question(qn_prompt[56], 'd'),
     Question(qn_prompt[57], 'a'),
     Question(qn_prompt[58], 'a'),
     Question(qn_prompt[59], 'b'),
     Question(qn_prompt[60], 'd'),
     Question(qn_prompt[61], 'c'),
     Question(qn_prompt[62], 'a'),
     Question(qn_prompt[63], 'b'),
     Question(qn_prompt[64], 'c'),
     Question(qn_prompt[65], 'a'),
     Question(qn_prompt[66], 'a'),
     Question(qn_prompt[67], 'd'),
     Question(qn_prompt[68], 'c'),
     Question(qn_prompt[69], 'b'),
]
