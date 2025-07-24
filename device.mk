
#
# Copyright (C) 2023 The Android Open Source Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from sm8475-common
$(call inherit-product, device/lenovo/sm8475-common/common.mk)

# Get non-open-source specific aspects
$(call inherit-product, vendor/lenovo/halo/halo-vendor.mk)

# Audio
PRODUCT_COPY_FILES += \
    $(LOCAL_PATH)/configs/audio/audio_effects.xml:$(TARGET_COPY_OUT_VENDOR)/etc/audio/sku_cape/audio_effects.xml \
    $(LOCAL_PATH)/configs/audio/mixer_paths_waipio_mtp.xml:$(TARGET_COPY_OUT_VENDOR)/etc/audio/sku_cape/mixer_paths_waipio_mtp.xml \
    $(LOCAL_PATH)/configs/audio/resourcemanager_waipio_mtp.xml:$(TARGET_COPY_OUT_VENDOR)/etc/audio/sku_cape/resourcemanager_waipio_mtp.xml \
    $(LOCAL_PATH)/configs/audio/usecaseKvManager.xml:$(TARGET_COPY_OUT_VENDOR)/etc/usecaseKvManager.xml

# Init
PRODUCT_COPY_FILES += \
    $(LOCAL_PATH)/init/init.class_main.sh:$(TARGET_COPY_OUT_VENDOR)/bin/init.class_main.sh \
    $(LOCAL_PATH)/init/init.halo.rc:$(TARGET_COPY_OUT_VENDOR)/etc/init/init.halo.rc \

# Keylayout
PRODUCT_COPY_FILES += \
    $(LOCAL_PATH)/configs/keylayout/goodix_ts.kl:$(TARGET_COPY_OUT_SYSTEM)/usr/keylayout/goodix_ts.kl

# Overlay
PRODUCT_PACKAGES += \
    CarrierConfigHalo \
    FrameworkResHalo \
    SystemUIResHalo \
    TelephonyResHalo \
    WifiResTargetHalo

# Parts
PRODUCT_PACKAGES += \
    LegionParts

# Soong namespaces
PRODUCT_SOONG_NAMESPACES += \
    $(LOCAL_PATH)
