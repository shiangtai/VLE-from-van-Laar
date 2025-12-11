import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from matplotlib.figure import Figure

# Function to calculate Gibbs free energy of mixing using van Laar model
def gibbs_free_energy_of_mixing(x1, alpha, beta):
    x2 = 1 - x1
    gamma_1, gamma_2 = activity_coefficients(x1, alpha, beta)
    G_mix = x1 * np.log(gamma_1 * x1) + x2 * np.log(gamma_2 * x2)
    return G_mix

# Function to calculate the activity coefficients
def activity_coefficients(x1, alpha, beta):
    x2 = 1 - x1
    lngamma_1 = alpha * ((beta * x2) / (alpha * x1 + beta * x2))**2
    lngamma_2 = beta * ((alpha * x1) / (alpha * x1 + beta * x2))**2
    return np.exp(lngamma_1), np.exp(lngamma_2)

# Function to calculate Pxy diagram
def calculate_pxy(x1_values, alpha, beta, P1_sat, P2_sat):
    gamma_1_values, gamma_2_values = activity_coefficients(x1_values, alpha, beta)
    
    # Bubble point pressure calculation
    P_bubble = x1_values * gamma_1_values * P1_sat + (1 - x1_values) * gamma_2_values * P2_sat
    
    # Vapor phase composition
    y1_values = (x1_values * gamma_1_values * P1_sat) / P_bubble
    
    return P_bubble, y1_values

# Function to update the plots
def update_plot(*args):
    alpha = alpha_slider.get()
    beta = beta_slider.get()
    P1_sat = P1_slider.get()
    P2_sat = P2_slider.get()
    
    x1_values = np.linspace(0.001, 0.999, 100)
    G_mix_values = gibbs_free_energy_of_mixing(x1_values, alpha, beta)
    gamma_1_values, gamma_2_values = activity_coefficients(x1_values, alpha, beta)
    G_mix_IM = x1_values * np.log( x1_values) + (1 - x1_values) * np.log(1 - x1_values)
    
    # Calculate Pxy diagram
    P_bubble, y1_values = calculate_pxy(x1_values, alpha, beta, P1_sat, P2_sat)
    
    # Update Gibbs Free Energy of Mixing plot
    ax1.clear()
    ax1.plot(x1_values, G_mix_values, label=f'$\Delta G_{{mix}}$(α={alpha:.2f}, β={beta:.2f})')
    ax1.plot(x1_values, G_mix_IM, label=r'$\Delta G_{mix}^{IM}$', linestyle='--')   
    ax1.set_xlabel("Mole fraction of component 1 ($x_1$)")
    ax1.set_ylabel("Gibbs Free Energy of Mixing ($\Delta G_{mix}$)")
    ax1.legend()
    ax1.grid(True)
    
    # Update Activity Coefficients plot
    ax2.clear()
    ax2.plot(x1_values, gamma_1_values, label=r'$\gamma_1$', color='b')
    ax2.plot(x1_values, gamma_2_values, label=r'$\gamma_2$', color='r')
    ax2.set_xlabel("Mole fraction of component 1 ($x_1$)")
    ax2.set_ylabel("Activity Coefficients ($\gamma$)")
    ax2.legend()
    ax2.grid(True)
    
    # Update Pxy phase diagram
    ax3.clear()
    ax3.plot(x1_values, P_bubble, label='Bubble point (liquid)', color='b', linewidth=2)
    ax3.plot(y1_values, P_bubble, label='Dew point (vapor)', color='r', linewidth=2)
    ax3.set_xlabel("Mole fraction of component 1 ($x_1, y_1$)")
    ax3.set_ylabel("Pressure (P)")
    ax3.set_title(f'$P_1^{{sat}}$={P1_sat:.2f}, $P_2^{{sat}}$={P2_sat:.2f}')
    ax3.legend()
    ax3.grid(True)
    
    # Update xy diagram
    ax4.clear()
    ax4.plot(x1_values, y1_values, label='y1', color='b', linewidth=2)
    ax4.plot(x1_values, x1_values, linestyle='--', color='gray', linewidth=2)
    ax4.set_xlabel("Mole fraction of component 1 ($x_1$)")
    ax4.set_ylabel("Mole fraction of component 1 ($y_1$)")
    ax4.set_title(f'$P_1^{{sat}}$={P1_sat:.2f}, $P_2^{{sat}}$={P2_sat:.2f}')
    ax4.legend()
    ax4.grid(True)

    canvas.draw()

# Initialize main window
root = tk.Tk()
root.title("Van Laar Model Parameter Visualization")

# Initialize figure and axes
fig = Figure(figsize=(8,7), dpi=100)
fig.suptitle("Vapor-Liquid Equilibrium using Van Laar Model", fontsize=16)
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

# Add tight_layout to automatically adjust spacing
# fig.tight_layout(rect=[0, 0, 1, 0.96])  # rect parameter leaves space for suptitle
# Manually adjust spacing
fig.subplots_adjust(left=0.1, right=0.95, top=0.93, bottom=0.08, hspace=0.35, wspace=0.3)

# Embed the plot in Tkinter Canvas
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Create a frame to hold sliders and place them horizontally
slider_frame = tk.Frame(root)
slider_frame.pack()

# Create sliders for alpha and beta parameters within the slider frame
alpha_slider = tk.Scale(slider_frame, from_=-5.0, to=5.0, resolution=0.1, orient="horizontal", label="Parameter α")
alpha_slider.set(1.0)  # Default value
alpha_slider.grid(row=0, column=0, padx=5, pady=5)
alpha_slider.bind("<Motion>", update_plot)

beta_slider = tk.Scale(slider_frame, from_=-5.0, to=5.0, resolution=0.1, orient="horizontal", label="Parameter β")
beta_slider.set(1.0)  # Default value
beta_slider.grid(row=0, column=1, padx=5, pady=5)
beta_slider.bind("<Motion>", update_plot)

P1_slider = tk.Scale(slider_frame, from_=0.01, to=10.0, resolution=0.1, orient="horizontal", label="P₁ˢᵃᵗ")
P1_slider.set(2.0)  # Default value
P1_slider.grid(row=0, column=2, padx=5, pady=5)
P1_slider.bind("<Motion>", update_plot)

P2_slider = tk.Scale(slider_frame, from_=0.1, to=10.0, resolution=0.1, orient="horizontal", label="P₂ˢᵃᵗ")
P2_slider.set(1.0)  # Default value
P2_slider.grid(row=0, column=3, padx=5, pady=5)
P2_slider.bind("<Motion>", update_plot)

# Initial plot update
update_plot()

# Run the Tkinter event loop
root.mainloop()
