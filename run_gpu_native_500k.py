"""
Helper entrypoint for fast GPU-native tests (5k steps, 500k atoms).
"""

from main_gpu_world_emergent_gpu_native import (
    EmergentConfig,
    run_lammps_simulation_gpu_native,
)


if __name__ == "__main__":
    cfg = EmergentConfig(n_steps=5_000)
    print("🚀 GPU-NATIVE BIOLOGY TEST - 5k Steps")
    print("Parameters: 500k particles, 5k steps, T=1.8, Ea=0.6")
    print("⚡ GPU-NATIVE: LAMMPS compute commands, single CPU sync at the end")
    run_lammps_simulation_gpu_native(cfg)
    print("✅ Short-run simulation complete! Check gpu_native.log for loop stats.")
