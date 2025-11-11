# Adaptive Layered Encryption using Graph-Based Path Optimization

## 📖 Overview
This project presents an **adaptive multi-layer encryption system** that integrates **graph theory** with **cryptographic techniques**.  
The goal is to secure data transmission in a network by dynamically adjusting the **encryption strength** based on the **number of hops (intermediate nodes)** between sender and receiver.

The system intelligently selects encryption layers depending on the path length — ensuring a balance between **speed and security**.

---

## Core Idea
In traditional encryption systems, the same encryption strength is used for all communications, regardless of how complex or long the path is.  
This project introduces **context-aware encryption**, where the system automatically adjusts encryption layers according to the **network topology**.

| Path Length (Hops) | Encryption Layers Used |
|---------------------|------------------------|
| 2 hops              | Caesar + Affine        |
| 3 hops              | Caesar + Affine + RSA  |
| ≥ 4 hops            | Caesar + Affine + RSA + Noise |

---

## Tech Stack
- **Language:** Python  
- **Libraries Used:**
  - `NetworkX` → Graph creation & shortest path determination  
  - `random` → Random key generation & noise layer  
  - *(Optional)* `matplotlib` → Graph visualization  
- **Core Concepts:** Graph Theory, Cryptography, Adaptive Algorithms, Modular Arithmetic

---

## Algorithms Implemented
- **Caesar Cipher** – Basic shift cipher  
- **Affine Cipher** – Linear transformation cipher  
- **RSA** – Public-key encryption for strong security  
- **Noise Layer** – Adds random distortion for unpredictability  
- **Graph Path Selection** – Uses `NetworkX` to determine shortest communication path  

---

## Methodology
1. **Graph Creation:** Define a network with nodes (users/routers) and edges (connections).  
2. **Path Selection:** Determine the shortest path between sender (Alice) and receiver (Bob).  
3. **Layer Selection:** Automatically decide encryption layers based on hop count.  
4. **Encryption:** Apply selected ciphers sequentially to the message.  
5. **Decryption:** Reverse the layers to retrieve the original message.  
6. **Validation:** Ensure 100% match between the original and decrypted message.

---

## Results and Discussion
- Encryption strength increases with the number of hops.  
- 100% decryption accuracy across all test cases.  
- Minimal computational overhead even for four-layer encryption.  
- Graph-based adaptivity ensures optimal performance for any network structure.  

---

## Security Highlights
- Demonstrates weaknesses of classical ciphers (Caesar, Affine).  
- Integrates RSA for robust public-key protection.  
- Adds noise-based randomization to resist frequency analysis.  
- Ensures adaptable, path-aware, and efficient cryptographic communication.

---

