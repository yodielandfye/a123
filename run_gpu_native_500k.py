"""
Helper entrypoint for fast GPU-native tests.
Now configured for a ~30-minute deep run (1,000,000 steps).
"""

from main_gpu_world_emergent_gpu_native import (
    EmergentConfig,
    run_lammps_simulation_gpu_native,
)


if __name__ == "__main__":
    # 1,000,000 steps ≈ 30 min at ~546 steps/s on the 5090
    cfg = EmergentConfig(n_steps=1_000_000)
    print("🚀 GPU-NATIVE BIOLOGY TEST - 1M Steps (~30 min)")
    print("Parameters: 500k particles, 1,000,000 steps, T=1.8, Ea=0.6")
    print("⚡ GPU-NATIVE: LAMMPS compute commands, single CPU sync at the end")
    run_lammps_simulation_gpu_native(cfg)
    print("✅ Long-run simulation complete! Check gpu_native.log for loop stats.")
