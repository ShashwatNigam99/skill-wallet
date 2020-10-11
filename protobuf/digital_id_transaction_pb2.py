# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuf/digital_id_transaction.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protobuf import digital_id_pb2 as protobuf_dot_digital__id__pb2
try:
  protobuf_dot_id__attribute__pb2 = protobuf_dot_digital__id__pb2.protobuf_dot_id__attribute__pb2
except AttributeError:
  protobuf_dot_id__attribute__pb2 = protobuf_dot_digital__id__pb2.protobuf.id_attribute_pb2
from protobuf import client_pb2 as protobuf_dot_client__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protobuf/digital_id_transaction.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n%protobuf/digital_id_transaction.proto\x1a\x19protobuf/digital_id.proto\x1a\x15protobuf/client.proto\"\xa7\x01\n\x14\x44igitalIdTransaction\x12\x12\n\ndigital_id\x18\x01 \x01(\x0c\x12\x17\n\x0fowner_signature\x18\x02 \x01(\t\x12\x17\n\x06status\x18\x03 \x01(\x0e\x32\x07.Status\x12\x1b\n\x13\x63\x65rtifier_signature\x18\x04 \x01(\t\x12,\n\x11owner_client_info\x18\x05 \x01(\x0b\x32\x11.ClientAttributesb\x06proto3')
  ,
  dependencies=[protobuf_dot_digital__id__pb2.DESCRIPTOR,protobuf_dot_client__pb2.DESCRIPTOR,])




_DIGITALIDTRANSACTION = _descriptor.Descriptor(
  name='DigitalIdTransaction',
  full_name='DigitalIdTransaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='digital_id', full_name='DigitalIdTransaction.digital_id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='owner_signature', full_name='DigitalIdTransaction.owner_signature', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='DigitalIdTransaction.status', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='certifier_signature', full_name='DigitalIdTransaction.certifier_signature', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='owner_client_info', full_name='DigitalIdTransaction.owner_client_info', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=92,
  serialized_end=259,
)

_DIGITALIDTRANSACTION.fields_by_name['status'].enum_type = protobuf_dot_id__attribute__pb2._STATUS
_DIGITALIDTRANSACTION.fields_by_name['owner_client_info'].message_type = protobuf_dot_client__pb2._CLIENTATTRIBUTES
DESCRIPTOR.message_types_by_name['DigitalIdTransaction'] = _DIGITALIDTRANSACTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DigitalIdTransaction = _reflection.GeneratedProtocolMessageType('DigitalIdTransaction', (_message.Message,), {
  'DESCRIPTOR' : _DIGITALIDTRANSACTION,
  '__module__' : 'protobuf.digital_id_transaction_pb2'
  # @@protoc_insertion_point(class_scope:DigitalIdTransaction)
  })
_sym_db.RegisterMessage(DigitalIdTransaction)


# @@protoc_insertion_point(module_scope)
