#!/data/data/com.termux/files/usr/bin/bash
# OMEGA FEDERATION: PERSISTENT RESURRECTION PROTOCOL
# This script ensures that model downloads resume automatically if interrupted.

cd ~/federation/models/incoming

# Function to pull with infinite retry and resume
pull_vessel() {
    local name=$1
    local url=$2
    echo "🚀 Initiating Omega-Stream for: $name"
    while true; do
        wget -c -O "$name" \
             --user-agent="Mozilla/5.0" \
             "$url"
        if [ $? -eq 0 ]; then
            echo "✅ $name secured."
            break
        else
            echo "⚠️ Signal lost. Re-initiating in 5 seconds..."
            sleep 5
        fi
    done
}

# ModelScope Mirrors (Bypassing the 401 Gate)
pull_vessel "SmolLM-1.7B-Instruct-Q4_K_M.gguf" \
            "https://modelscope.cn/api/v1/models/prithivMLmods/SmolLM-1.7B-Instruct-GGUF/repo?Revision=master&FilePath=SmolLM-1.7B-Instruct-Q4_K_M.gguf"

pull_vessel "Qwen2.5-1.8B-Instruct-Q4_K_M.gguf" \
            "https://modelscope.cn/api/v1/models/Qwen/Qwen2.5-1.8B-Instruct-GGUF/repo?Revision=master&FilePath=qwen2.5-1.8b-instruct-q4_k_m.gguf"

pull_vessel "Baichuan-2-1.3B-Chat-Q4_K_M.gguf" \
            "https://modelscope.cn/api/v1/models/mradermacher/Baichuan2-1.3B-Chat-GGUF/repo?Revision=master&FilePath=Baichuan2-1.3B-Chat-Q4_K_M.gguf"

pull_vessel "Yi-1.5-6B-Chat-Q4_K_M.gguf" \
            "https://modelscope.cn/api/v1/models/mradermacher/Yi-1.5-6B-Chat-GGUF/repo?Revision=master&FilePath=Yi-1.5-6B-Chat.Q4_K_M.gguf"

echo "🏁 All vessels secured in the incoming bay."
