# test_thresholds.py
from dual_ai_test import check_seed_usage

# Generate 16K token fragment (25% of 64K)
test_fragment_16k = "x" * (16000 * 4)  # 64,000 characters
warning_25 = check_seed_usage(len(test_fragment_16k) // 4)
print("25% Test Result:", warning_25)
assert "25%" in warning_25, "25% Test failed!"

# NEW: Generate 32K token fragment (50% of 64K)
test_fragment_32k = "y" * (32000 * 4)  # 128,000 characters
warning_50 = check_seed_usage(len(test_fragment_32k) // 4)
print("\n50% Test Result:", warning_50)  # Added newline for clarity
assert "50%" in warning_50, "50% Test failed!"
print("✅ Both 25% and 50% tests passed!")

# Add to test_thresholds.py after existing tests

# Generate 48K token fragment (75% of 64K)
test_fragment_48k = "z" * (48000 * 4)  # 192,000 characters
warning_75 = check_seed_usage(len(test_fragment_48k) // 4)
print("\n75% Test Result:", warning_75)
assert "75%" in warning_75, "75% Test failed!"

# Generate 64K token fragment (100% of 64K)
test_fragment_64k = "w" * (64000 * 4)  # 256,000 characters
warning_100 = check_seed_usage(len(test_fragment_64k) // 4)
print("\n100% Test Result:", warning_100)
assert "100%" in warning_100 and "🛑 CRITICAL" in warning_100, "100% Test failed!"

print("✅ ALL TESTS PASSED!")