Title: Wake Your Computer by USB
Date: 2008-07-14T20:27:57
Tags: ubuntu, Linux
Category: Tech

I recently began using my laptop at my desk with a USB keyboard and mouse, 
and I thought I would explain how to set up Ubuntu so that USB peripherals 
will wake up your computer from sleep mode. This is convenient if you have 
your laptop set up such that the lid is closed and inaccessible.

In Ubuntu, the way to set this up is to edit the file located at 
`/proc/acpi/wakeup`. To see the current contents of this file do this:

    :::bash
    % cat /proc/acpi/wakeup
    Device	S-state	  Status   Sysfs node
    P0P2	  S4	 disabled  
    P0P1	  S4	 disabled  pci:0000:00:1e.0
    MC97	  S4	 disabled  
    HDAC	  S4	 disabled  pci:0000:00:1b.0
    P0P4	  S4	 disabled  pci:0000:00:1c.0
    P0P5	  S4	 disabled  pci:0000:00:1c.1
    P0P7	  S4	 disabled  
    P0P8	  S4	 disabled  
    P0P9	  S4	 disabled  
    USB0	  S3	 disabled  pci:0000:00:1d.0
    USB1	  S3	 disabled  pci:0000:00:1d.1
    USB2	  S3	 disabled  pci:0000:00:1d.2
    USB3	  S3	 disabled  pci:0000:00:1d.3
    EUSB	  S3	 disabled  pci:0000:00:1d.7
    P0P6	  S4	 disabled  pci:0000:00:1c.2
    SLPB	  S4	*enabled

This shows you a number of devices, most of which I don't claim to 
understand. The ones to notice are the USB ones, which you will see are 
disabled by default.

Once these are toggled on, your computer will wake up from sleep when USB 
peripherals are used. To toggle one of these on, as root, run:

    :::bash
    echo "USB0" > /proc/acpi/wakeup

This will toggle USB0 from disabled to enabled. To check this, 
run `cat /proc/acpi/wakeup` again. You should see that it's enabled, 
and you should be able to test this by suspending your computer.

This will set up your computer to wake up from USB...for now. To make it 
work after your computer has been restarted, you will need to write a short 
init script named wake.sh with the following contents:

    :::bash
    #!/bin/bash
    echo "USB0" > /proc/acpi/wakeup
    
Save this file to `/etc/init.d`, and make it executable by running:

    :::bash
    chmod +x wake.sh

Finally, once this file is in `/etc/init.d`, and is executable, 
as root run:

    :::bash
    update-rc.d wake.sh defaults

That will make init know about the file, and run it at startup. Happy 
awakenings!

**Source:** <a href="http://ubuntuforums.org/showthread.php?t=711747">http://ubuntuforums.org/showthread.php?t=711747</a>

