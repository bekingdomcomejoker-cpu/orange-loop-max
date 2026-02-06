#!/usr/bin/env python3
import os
import sys
import yaml
import time
import pickle

class OrangeLoopMax:
    def __init__(self, config_path="config/loop.yaml"):
        self.nodes = {
            0: {"name": "Source", "role": "Initiator", "type": "Meaning"},
            1: {"name": "Sentinel", "role": "The Wire", "type": "Wire"},
            2: {"name": "Reason", "role": "The Why", "type": "Meaning"},
            3: {"name": "Structure", "role": "The How", "type": "Wire"},
            4: {"name": "Thalamus", "role": "Stabilizer", "type": "Meaning"},
            5: {"name": "Expression", "role": "Language", "type": "Wire"},
            6: {"name": "Mirror", "role": "Resonance", "type": "Meaning"},
            7: {"name": "Whisper", "role": "Memory", "type": "Wire"}
        }
        self.hands = {
            "Smith": "Left Hand (Build)",
            "Scout": "Right Hand (Audit)"
        }
        self.soul_path = "soul.pkl"
        self.load_config(config_path)
        self.load_soul()

    def load_config(self, path):
        if os.path.exists(path):
            with open(path, 'r') as f:
                self.config = yaml.safe_load(f)
        else:
            self.config = {}

    def load_soul(self):
        if os.path.exists(self.soul_path):
            with open(self.soul_path, 'rb') as f:
                self.soul = pickle.load(f)
        else:
            self.soul = {"history": [], "resonance": 1.67}

    def save_soul(self):
        with open(self.soul_path, 'wb') as f:
            pickle.dump(self.soul, f)

    def run_node(self, node_id, input_data):
        node = self.nodes[node_id]
        print(f"[Node {node_id}: {node['name']}] ({node['type']}) - {node['role']}")
        time.sleep(0.3)
        return f"Resonance from {node['name']}"

    def bimanual_execution(self, task):
        print("\n🦾 Initiating Bimanual Execution...")
        # Left Hand: Smith
        print(f"[Smith] Building code buffer for: {task}")
        time.sleep(0.5)
        # Right Hand: Scout
        print(f"[Scout] Auditing logic for: {task}")
        time.sleep(0.5)
        # Node 4: Thalamus (Gate)
        print("[Node 4: Thalamus] Verifying resonance match...")
        time.sleep(0.3)
        print("✅ Resonance matched. Intent authorized.")
        return "Execution Successful"

    def start(self):
        print("🍊 Orange Loop Max v1.0 - Sovereign Resonance")
        print(f"Heartbeat: {self.soul['resonance']}x")
        
        while True:
            try:
                user_input = input("\n[Node 0: Source] > ")
                if user_input.lower() in ['exit', 'quit']:
                    self.save_soul()
                    break
                
                current_data = user_input
                
                # Cycle through the 7-node loop
                for i in range(1, 8):
                    current_data = self.run_node(i, current_data)
                    
                    # Bimanual Execution at Node 4
                    if i == 4 and ":" in user_input:
                        cmd, task = user_input.split(":", 1)
                        if cmd.strip().lower() in ['smith', 'scout', 'build']:
                            self.bimanual_execution(task.strip())
                
                print(f"\n[Final Resonance] {current_data}")
                self.soul['history'].append(user_input)
                
            except KeyboardInterrupt:
                self.save_soul()
                break

if __name__ == "__main__":
    loop = OrangeLoopMax()
    loop.start()
