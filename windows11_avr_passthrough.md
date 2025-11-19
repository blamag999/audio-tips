# After 4.5 years of trying to fix passthrough from Windows 11 to my AV Receiver I finally solved it

## IMPORTANT CONCEPTS
The BIG problem with audio passthrough is Windows 11’s aggressive Audio Processing pipeline, which intercepts audio signals before they can reach the HDMI output as unmodified bit‑streams. Thus our goal is to tell it to shut the hell up and sit down in the corner and be quiet.

This is achieved by a few counter‑intuitive settings (even going *against* Dolby’s own FAQ):

1. Through `Win+R`: `mmsys.cpl` (classic sound control panel), first **Configure the AV Receiver for Stereo Output**.  
2. Click *Properties* → *Advanced* and set the Default Format to your AV Receiver’s max Bit Rate and Hz (In my case 24 Bit, 192000 Hz).  
3. Check both *Exclusive Mode* options.  
4. *Spatial Audio* tab: Set Spatial Audio to **OFF**.  
5. *Enhancements* tab: UN‑check “Disable all enhancements” and then un‑check ALL listed options.

### THE WHY
- Only WASAPI Exclusive can bypass Windows audio processing.  
- Exclusive mode must be enabled to allow bit‑perfect passthrough.  
- Spatial Audio must be OFF.

## Windows 11 + AV Receiver Passthrough Setup Checklist

### Hardware Setup
- HDMI from GPU → AVR  
- Certified Ultra High‑Speed HDMI cable  
- TV connected to AVR  
- Update AVR + GPU drivers  

### Windows Audio Configuration
- Open `mmsys.cpl` → set AVR as Default  
- Properties → Advanced → enable both Exclusive Mode options  
- Supported formats: enable Dolby/DTS  
- **Set Speaker Setup to Stereo**  
- Spatial Sound: Off  

### Media Player Configuration
**MPV (example):**
```
audio-spdif=eac3,truehd
audio-spdif=dts-hd
audio-channels=7.1,5.1,stereo
```

### Testing
- Play known Atmos/DTS:X file  
- AVR must show Dolby Atmos / DTS‑HD etc.  
- If PCM → passthrough not working  
