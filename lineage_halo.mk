#
# Copyright (C) 2024 The Android Open Source Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit some common Lineage stuff.
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

# Inherit from halo device.
$(call inherit-product, device/lenovo/halo/device.mk)

## Device identifier
PRODUCT_DEVICE := halo
PRODUCT_NAME := lineage_halo
PRODUCT_BRAND := lenovo
PRODUCT_MODEL := Legion Y70
PRODUCT_MANUFACTURER := lenovo

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc=$(call normalize-path-list, "Lenovo halo halo 13 TKQ1.221114.001 L71091_CN_SECURE_USER_Q00031.0_T_ZUI_15.0.375_ST_240403:user release-keys")

BUILD_FINGERPRINT := Lenovo/halo/halo:13/TKQ1.221114.001/L71091_CN_SECURE_USER_Q00031.0_T_ZUI_15.0.375_ST_240403:user/release-keys

# GMS
PRODUCT_GMS_CLIENTID_BASE := android-lenovo