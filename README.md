# Van Laar Model Interactive Visualization

An interactive Python application for visualizing the van Laar thermodynamic model for binary liquid mixtures, including Gibbs free energy of mixing, activity coefficients, pressure-composition (Pxy), and composition (y-x) phase diagrams.

## Features

- **Interactive Parameter Control**: Real-time adjustment of van Laar parameters (α, β) and vapor pressures using sliders
- **Three Simultaneous Visualizations**:
  - Gibbs Free Energy of Mixing (ΔG_mix)
  - Activity Coefficients (γ₁, γ₂)
  - Pressure-Composition (Pxy) Phase Diagram with bubble and dew point curves
  - vapor-phase composition vs liquid phase composition (xy) phase diagrams
- **Educational Tool**: Demonstrates the relationship between model parameters and phase behavior in non-ideal binary mixtures

## Screenshots

![Van Laar Model Visualization]([Screenshot%202025-12-11%20154441.png]

## Requirements
```
numpy
matplotlib
tkinter (usually included with Python)
```

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/van-laar-visualization.git
cd van-laar-visualization
```

2. Install required packages:
```bash
pip install numpy matplotlib
```

## Usage

Run the main script:
```bash
python vanLaar-improved.py
```

### Interactive Controls

- **Parameter α**: Van Laar parameter for component 1 (range: 0.1 - 5.0)
- **Parameter β**: Van Laar parameter for component 2 (range: 0.1 - 5.0)
- **P₁ˢᵃᵗ**: Vapor pressure of component 1 (range: 0.1 - 10.0)
- **P₂ˢᵃᵗ**: Vapor pressure of component 2 (range: 0.1 - 10.0)

Move the sliders to see real-time updates in all three plots.

## Theory

### Van Laar Model

The van Laar model describes the activity coefficients in non-ideal binary mixtures:
```
ln γ₁ = α * [β * x₂ / (α * x₁ + β * x₂)]²
ln γ₂ = β * [α * x₁ / (α * x₁ + β * x₂)]²
```

### Gibbs Free Energy of Mixing
```
ΔG_mix = x₁ * ln(γ₁ * x₁) + x₂ * ln(γ₂ * x₂)
```

### Pxy Phase Diagram

The bubble point pressure is calculated using modified Raoult's law:
```
P_bubble = x₁ * γ₁ * P₁ˢᵃᵗ + x₂ * γ₂ * P₂ˢᵃᵗ
```

Vapor composition:
```
y₁ = (x₁ * γ₁ * P₁ˢᵃᵗ) / P_bubble
```

## Educational Applications

This tool is useful for:
- Chemical engineering thermodynamics courses
- Understanding non-ideal solution behavior
- Visualizing liquid-liquid and vapor-liquid equilibria
- Exploring the effects of interaction parameters on phase behavior
- Demonstrating the relationship between activity coefficients and phase diagrams

## File Structure
```
van-laar-visualization/
│
├── vanLaar-improved.py           # Main application script
├── README.md                     # This file
├── LICENSE                       # License file

```

## Examples

### Example 1: Ideal Solution
Set α = 0.1 and β = 0.1 to approximate ideal behavior (γ₁ ≈ γ₂ ≈ 1)

### Example 2: Positive Deviation
Set α = 2.5 and β = 2.5 to see positive deviation from Raoult's law

### Example 3: Asymmetric System
Set α = 3.0 and β = 1.5 to explore asymmetric behavior

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Future Enhancements

- [ ] Add temperature slider for temperature-dependent vapor pressures
- [ ] Include liquid-liquid equilibrium detection
- [ ] Export data to CSV
- [ ] Add other activity coefficient models (NRTL, UNIQUAC)
- [ ] 3D visualization of Gibbs energy surface

## License

This project is licensed under the MIT License 

## Author

**Shiang-Tai**
- GitHub: [@shiangtai](https://github.com/shiangtai)
- Repository: [myPython](https://github.com/shiangtai/VLE-from-van-Laar)

## Acknowledgments

- Based on fundamental thermodynamic principles from chemical engineering
- Developed for educational purposes at National Taiwan University
- Built with Python, NumPy, and Matplotlib

## Contact

For questions or suggestions, please open an issue on GitHub or contact [stlin@ntu.edu.tw].

---

*Made with ❤️ for chemical engineering education*
