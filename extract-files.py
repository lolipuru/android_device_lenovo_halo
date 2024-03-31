#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

import extract_utils.tools
from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/lenovo/halo',
    'device/lenovo/sm8475-common',
    'hardware/qcom-caf/sm8450',
    'vendor/qcom/opensource/commonsys-intf/display',
    'vendor/lenovo/sm8475-common',
]

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'libagmclient',
        'libagmmixer',
        'libpalclient',
        'libagm',
        'libats',
        'libar-acdb',
        'libar-pal',
        'libar-gsl',
        'liblx-osal',
        'vendor.qti.hardware.pal@1.0-impl',
        'libDummySnapshotAlgorithm',
    ): lib_fixup_remove,
}

blob_fixups: blob_fixups_user_type = {
    (
        'vendor/bin/hw/qfp-daemon',
        'vendor/lib64/libqfp-service.so',): blob_fixup()
        .replace_needed(
            'android.hardware.biometrics.common-V1-ndk_platform.so',
            'android.hardware.biometrics.common-V1-ndk.so',
        )
        .replace_needed(
            'android.hardware.biometrics.fingerprint-V1-ndk_platform.so',
            'android.hardware.biometrics.fingerprint-V1-ndk.so',
        ),
    ('vendor/lib64/libQnnGpu.so',): blob_fixup()
        .strip_debug_sections(),
    ('vendor/lib64/libcamximageformatutils.so'): blob_fixup()
        .replace_needed(
            'vendor.qti.hardware.display.config-V2-ndk_platform.so',
            'vendor.qti.hardware.display.config-V2-ndk.so',
        ),
    (
        'vendor/bin/hw/android.hardware.gnss-aidl-service-qti',
        'vendor/lib64/hw/android.hardware.gnss-aidl-impl-qti.so',
        'vendor/lib64/libgarden.so',
        'vendor/lib64/libgarden_haltests_e2e.so',
    ): blob_fixup()
        .replace_needed(
            'android.hardware.gnss-V1-ndk_platform.so',
            'android.hardware.gnss-V1-ndk.so',
        ),
    (
        'vendor/lib64/libpandora.render.so',
    ): blob_fixup()
        .clear_symbol_version('AHardwareBuffer_allocate')
        .clear_symbol_version('AHardwareBuffer_describe')
        .clear_symbol_version('AHardwareBuffer_lockPlanes')
        .clear_symbol_version('AHardwareBuffer_release')
        .clear_symbol_version('AHardwareBuffer_unlock'),
    (
        'vendor/lib64/nfc_nci.nqx.default.hw.so',
    ): blob_fixup()
        .add_needed('libbase_shim.so'),
    (
        'vendor/bin/hw/dolbycodec2',
        'vendor/bin/hw/vendor.dolby.hardware.dms@2.0-service',
        'vendor/bin/hw/vendor.dolby.media.c2@1.0-service',
    ): blob_fixup()
        .add_needed('libstagefright_foundation-v33.so'),
    (
        'vendor/lib/c2.dolby.client.so',
        'vendor/lib64/c2.dolby.client.so',
    ): blob_fixup()
        .add_needed('dolbycodec_shim.so'),
}

module = ExtractUtilsModule(
    'halo',
    'lenovo',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
    check_elf=True,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(
        module, 'sm8475-common', module.vendor
    )
    utils.run()