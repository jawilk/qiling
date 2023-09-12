#!/usr/bin/env python3
# 
# Cross Platform and Multi Architecture Advanced Binary Emulation Framework
#

from qiling.os.const import *
from ..fncc import *
from ..ProcessorBind import *
from ..UefiBaseType import *


# 1st arg return type, then func argument types
EFI_ASYNC_USB_TRANSFER_CALLBACK = FUNCPTR(EFI_STATUS, VOID, UINTN, VOID, UINT32)

### API
# Note 2nd arg VOID = EFI_USB_IO_PROTOCOL
EFI_USB_IO_CONTROL_TRANSFER = FUNCPTR(EFI_STATUS, VOID, EFI_USB_DEVICE_REQUEST, EFI_USB_DATA_DIRECTION, UINT32, VOID, UINTN, UINT32)

EFI_USB_IO_BULK_TRANSFER = FUNCPTR(EFI_STATUS, VOID, UINT8, VOID, UINTN, UINTN, UINT32)

EFI_USB_IO_ASYNC_INTERRUPT_TRANSFER = FUNCPTR(EFI_STATUS, VOID, UINT8, BOOLEAN, UINTN, UINTN, EFI_ASYNC_USB_TRANSFER_CALLBACK, VOID)

EFI_USB_IO_SYNC_INTERRUPT_TRANSFER = FUNCPTR(EFI_STATUS, VOID, UINT8, VOID, UINTN, UINTN, UINT32)

EFI_USB_IO_ISOCHRONOUS_TRANSFER = FUNCPTR(EFI_STATUS, VOID, UINT8, VOID, UINTN, UINT32)

EFI_USB_IO_ASYNC_ISOCHRONOUS_TRANSFER = FUNCPTR(EFI_STATUS, VOID, UINT8, VOID, UINTN, EFI_ASYNC_USB_TRANSFER_CALLBACK, VOID)

EFI_USB_IO_GET_DEVICE_DESCRIPTOR = FUNCPTR(EFI_STATUS, VOID, EFI_USB_DEVICE_DESCRIPTOR)

EFI_USB_IO_GET_CONFIG_DESCRIPTOR = FUNCPTR(EFI_STATUS, VOID, EFI_USB_CONFIG_DESCRIPTOR)

EFI_USB_IO_GET_INTERFACE_DESCRIPTOR = FUNCPTR(EFI_STATUS, VOID, EFI_USB_INTERFACE_DESCRIPTOR)

EFI_USB_IO_GET_ENDPOINT_DESCRIPTOR = FUNCPTR(EFI_STATUS, VOID, UINT8, EFI_USB_ENDPOINT_DESCRIPTOR)

EFI_USB_IO_GET_STRING_DESCRIPTOR = FUNCPTR(EFI_STATUS, VOID, UINT16, UINT8, CHAR16)

EFI_USB_IO_GET_SUPPORTED_LANGUAGE = FUNCPTR(EFI_STATUS, VOID, UINT16, UINT16)


class USB_IO_PROTOCOL(STRUCT):
	_fields_ = [
		('UsbControlTransfer', EFI_USB_IO_CONTROL_TRANSFER),
		('UsbBulkTransfer',	EFI_USB_IO_BULK_TRANSFER),
		('UsbAsyncInterruptTransfer', EFI_USB_IO_ASYNC_INTERRUPT_TRANSFER),
		('UsbSyncInterruptTransfer', EFI_USB_IO_SYNC_INTERRUPT_TRANSFER),
		('UsbIsochronousTransfer', EFI_USB_IO_ISOCHRONOUS_TRANSFER),
		('UsbAsyncIsochronousTransfer',	EFI_USB_IO_ASYNC_ISOCHRONOUS_TRANSFER),
		('UsbGetDeviceDescriptor', EFI_USB_IO_GET_DEVICE_DESCRIPTOR),
		('UsbGetConfigDescriptor', EFI_USB_IO_GET_CONFIG_DESCRIPTOR),
		('UsbGetInterfaceDescriptor', EFI_USB_IO_GET_INTERFACE_DESCRIPTOR),
		('UsbGetEndpointDescriptor', EFI_USB_IO_GET_ENDPOINT_DESCRIPTOR),
		('UsbGetStringDescriptor', EFI_USB_IO_GET_STRING_DESCRIPTOR),
		('UsbGetSupportedLanguages', EFI_USB_IO_GET_SUPPORTED_LANGUAGE)
	]
	
@dxeapi(params = {
	"SkuId" : UINT
})
def hook_UsbControlTransfer(ql, address, params):
	pass

@dxeapi(params = {
	"SkuId" : UINT
})

def hook_UsbBulkTransfer(ql, address, params):
	pass

@dxeapi(params = {
	"SkuId" : UINT
})

def hook_UsbAsyncInterruptTransfer(ql, address, params):
	pass

@dxeapi(params = {
	"SkuId" : UINT
})
def hook_UsbSyncInterruptTransfer(ql, address, params):
	pass

@dxeapi(params = {
	"SkuId" : UINT
})
def hook_UsbIsochronousTransfer(ql, address, params):
	pass

@dxeapi(params = {
	"SkuId" : UINT
})
def hook_UsbAsyncIsochronousTransfer(ql, address, params):
	pass

@dxeapi(params = {
	"SkuId" : UINT
})
def hook_UsbGetDeviceDescriptor(ql, address, params):
	pass

@dxeapi(params = {
	"SkuId" : UINT
})
def hook_UsbGetConfigDescriptor(ql, address, params):
	pass

@dxeapi(params = {
	"SkuId" : UINT
})
def hook_UsbGetInterfaceDescriptor(ql, address, params):
	pass

@dxeapi(params = {
	"SkuId" : UINT
})
def hook_UsbGetEndpointDescriptor(ql, address, params):
	pass

@dxeapi(params = {
	"SkuId" : UINT
})
def hook_UsbGetStringDescriptor(ql, address, params):
	pass

@dxeapi(params = {
	"SkuId" : UINT
})
def hook_UsbGetSupportedLanguages(ql, address, params):
	pass


@dxeapi(params = {
	"SkuId" : UINT
})
def hook_UsbAsyncTransferCallback(ql, address, params):
	pass

@dxeapi(params = {
	"TokenNumber" : UINT
})
def hook_UsbAsyncInterruptTransfer(ql, address, params):
	pass

descriptor = {
	"guid" : "2b2f68d6-0cd2-44cf-8e8b-bba20b1b5b75",
	"struct" : USB_IO_PROTOCOL,
	"fields" : (
		('UsbControlTransfer', hook_UsbControlTransfer),
		('UsbBulkTransfer', hook_UsbBulkTransfer),
		('UsbAsyncInterruptTransfer', hook_UsbAsyncInterruptTransfer),
		('UsbSyncInterruptTransfer', hook_UsbSyncInterruptTransfer),
		('UsbIsochronousTransfer', hook_UsbIsochronousTransfer),
		('UsbAsyncIsochronousTransfer', hook_UsbAsyncIsochronousTransfer),
		('UsbGetDeviceDescriptor', hook_UsbGetDeviceDescriptor),
		('UsbGetConfigDescriptor', hook_UsbGetConfigDescriptor),
		('UsbGetInterfaceDescriptor', hook_UsbGetInterfaceDescriptor),
		('UsbGetEndpointDescriptor', hook_UsbGetEndpointDescriptor),
		('UsbGetStringDescriptor', hook_UsbGetStringDescriptor),
        ('UsbGetSupportedLanguages', hook_UsbGetSupportedLanguages),
	)
}
