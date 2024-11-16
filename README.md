# Energy Efficient Accurate and Approximate Modified Adders for Ternary Multipliers
Accepted in ISCAS-2024
Authors : L Hemanth Krishna and Dr. B. Srinivasu
This repository provides the implementation of energy-efficient approximate multiplier designs using proposed modified adder designs. The work is based on the paper titled:

> *"Energy-Efficient Approximate Multiplier Designs Using Proposed Modified Adder Designs"*

## Overview

In this project, we propose accurate and approximate designs for modified half adders (MHA) and full adders (FA1 and FA2) using a combination of 3×1 and 2×1 multiplexers. These designs demonstrate significant energy savings compared to conventional adders and multipliers.

### Key Contributions:
1. **Modified Half-Adder (MHA):**
   - Consumes **63.2% less energy** than the conventional half-adder.
2. **Modified Full Adders:**
   - FA1 saves **24% energy** compared to the conventional full adder.
   - FA2 saves **44% energy** compared to the conventional full adder.
3. **Approximate Multiplier:**
   - Saves **26% energy** compared to a conventional full adder-based multiplier.

### Applications:
The proposed designs were tested on image processing tasks, such as image multiplication. Results demonstrate improved:
- **Peak Signal-to-Noise Ratio (PSNR)**
- **Structural Similarity Index Measure (SSIM)**

---

## Simulation Environment

### Tools and Technologies:
- **Synopsys HSPICE:** Used for simulations.
- **MOSFET-like CNFET:** Employed for transistor-level simulations.

---

## Implementation Details

### Adders:
- **Modified Half-Adder (MHA):** Designed with energy efficiency in mind.
- **Full Adders FA1 and FA2:** Optimized for energy savings and accuracy.

### Multiplier:
- Constructed using the proposed adders, demonstrating both energy efficiency and effectiveness in practical applications.

### Image Processing:
- The designs were evaluated for tasks such as image multiplication, showcasing superior PSNR and SSIM over existing designs.

---

## Results

### Energy Savings:
| Component            | Energy Savings (%) |
|----------------------|--------------------|
| Modified Half-Adder  | 63.2%             |
| Full Adder FA1       | 24%               |
| Full Adder FA2       | 44%               |
| Approximate Multiplier | 26%               |

### Image Quality:
- **PSNR:** Improved performance over existing designs.
- **SSIM:** Higher structural similarity compared to alternatives.

---

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/hemanth-abhi850/Ternary-multiplier.git
   
##Reference
This project is licensed under the MIT License

If you use these designs in your work, please cite the following:

https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10558406
