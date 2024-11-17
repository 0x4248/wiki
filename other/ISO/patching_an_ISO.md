# Patching an ISO

In this guide I will show you how to patch an ISO file. Since ISO files are not writable, we will have to mount the ISO, modify the contents, and then create a new ISO file using the modified contents.

## Prerequisites

- A Linux system
- `genisoimage` package

### Installing `genisoimage`

#### Debian-based systems

To install `genisoimage` on debian-based systems, run the following command:

```bash
sudo apt-get install genisoimage
```

#### Arch-based systems

To install `genisoimage` on arch-based systems, run the following command:

```bash
sudo pacman -S cdrtools
```

#### Fedora-based systems

To install `genisoimage` on fedora-based systems, run the following command:

```bash
sudo dnf install genisoimage
```

## Steps

1. Create a directory to mount the ISO file:

```bash
mkdir /mnt/iso
```

2. Mount the ISO file:

```bash
sudo mount -o loop file.iso /mnt/iso
```

3. Modify the contents of the mounted ISO file as needed.

4. Create a new ISO file with the modified contents:

```bash
genisoimage -o newfile.iso -r -J /mnt/iso
```

5. Unmount the ISO file:

```bash
sudo umount /mnt/iso
```

Now you have successfully patched an ISO file.