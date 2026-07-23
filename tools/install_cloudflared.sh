#!/bin/bash
echo "=== Installing Cloudflare Tunnel (cloudflared) on Linux Mint ==="
echo ""

# Remove the broken repo entry first
sudo rm -f /etc/apt/sources.list.d/cloudflared.list

# Download the .deb package directly
wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb -O /tmp/cloudflared.deb
sudo dpkg -i /tmp/cloudflared.deb
rm /tmp/cloudflared.deb

echo ""
cloudflared --version
echo ""
echo "=== Done! Now run: cloudflared tunnel login ==="
