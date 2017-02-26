#!/bin/sh

# args
dir="$1"

# cfg
shell="$dir/Shell.efi"
enroll="$dir/EnrollDefaultKeys.efi"
vfat="$dir/shell.img"
iso="$dir/UefiShell.iso"
export MTOOLS_SKIP_CHECK=1

# calc size
s1=$(stat --format=%s -- $shell)
s2=$(stat --format=%s -- $enroll)
size=$(( ($s1 + $s2) * 11 / 10 ))
set -x

# create non-partitioned FAT image
/usr/sbin/mkdosfs -C "$vfat" -n UEFI_SHELL -- "$(( $size / 1024 ))"
mmd	-i "$vfat"			::efi
mmd	-i "$vfat"			::efi/boot
mcopy	-i "$vfat"	"$shell"	::efi/boot/bootx64.efi
mcopy	-i "$vfat"	"$enroll"	::
#mdir	-i "$vfat"	-/		::

# build ISO with FAT image file as El Torito EFI boot image
genisoimage -input-charset ASCII -J -rational-rock \
	-efi-boot "${vfat##*/}" -no-emul-boot -o "$iso" -- "$vfat"
rm -f "$vfat"
