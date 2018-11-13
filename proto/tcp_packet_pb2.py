# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tcp_packet.proto

import sys
_b = sys.version_info[0] < 3 and (
    lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import proto.player_pb2 as player__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name='tcp_packet.proto',
    package='',
    syntax='proto2',
    serialized_options=None,
    serialized_pb=_b('\n\x10tcp_packet.proto\x1a\x0cplayer.proto\"\x8a\x08\n\tTcpPacket\x12#\n\x04type\x18\x01 \x02(\x0e\x32\x15.TcpPacket.PacketType\x1a\xa4\x01\n\x10\x44isconnectPacket\x12#\n\x04type\x18\x01 \x02(\x0e\x32\x15.TcpPacket.PacketType\x12\x17\n\x06player\x18\x02 \x01(\x0b\x32\x07.Player\x12\x32\n\x06update\x18\x03 \x01(\x0e\x32\".TcpPacket.DisconnectPacket.Update\"\x1e\n\x06Update\x12\n\n\x06NORMAL\x10\x00\x12\x08\n\x04LOST\x10\x01\x1a\xad\x01\n\rConnectPacket\x12#\n\x04type\x18\x01 \x02(\x0e\x32\x15.TcpPacket.PacketType\x12\x17\n\x06player\x18\x02 \x02(\x0b\x32\x07.Player\x12\x10\n\x08lobby_id\x18\x03 \x01(\t\x12/\n\x06update\x18\x04 \x01(\x0e\x32\x1f.TcpPacket.ConnectPacket.Update\"\x1b\n\x06Update\x12\x08\n\x04SELF\x10\x00\x12\x07\n\x03NEW\x10\x01\x1a_\n\x11\x43reateLobbyPacket\x12#\n\x04type\x18\x01 \x02(\x0e\x32\x15.TcpPacket.PacketType\x12\x10\n\x08lobby_id\x18\x02 \x01(\t\x12\x13\n\x0bmax_players\x18\x03 \x01(\x05\x1am\n\nChatPacket\x12#\n\x04type\x18\x01 \x02(\x0e\x32\x15.TcpPacket.PacketType\x12\x0f\n\x07message\x18\x02 \x02(\t\x12\x17\n\x06player\x18\x03 \x01(\x0b\x32\x07.Player\x12\x10\n\x08lobby_id\x18\x04 \x01(\t\x1aU\n\x10PlayerListPacket\x12#\n\x04type\x18\x01 \x02(\x0e\x32\x15.TcpPacket.PacketType\x12\x1c\n\x0bplayer_list\x18\x03 \x03(\x0b\x32\x07.Player\x1aI\n\rErrLdnePacket\x12#\n\x04type\x18\x01 \x02(\x0e\x32\x15.TcpPacket.PacketType\x12\x13\n\x0b\x65rr_message\x18\x02 \x01(\t\x1aJ\n\x0e\x45rrLfullPacket\x12#\n\x04type\x18\x01 \x02(\x0e\x32\x15.TcpPacket.PacketType\x12\x13\n\x0b\x65rr_message\x18\x02 \x01(\t\x1a\x45\n\tErrPacket\x12#\n\x04type\x18\x01 \x02(\x0e\x32\x15.TcpPacket.PacketType\x12\x13\n\x0b\x65rr_message\x18\x02 \x02(\t\"|\n\nPacketType\x12\x0e\n\nDISCONNECT\x10\x00\x12\x0b\n\x07\x43ONNECT\x10\x01\x12\x10\n\x0c\x43REATE_LOBBY\x10\x02\x12\x08\n\x04\x43HAT\x10\x03\x12\x0f\n\x0bPLAYER_LIST\x10\x04\x12\x0c\n\x08\x45RR_LDNE\x10\x05\x12\r\n\tERR_LFULL\x10\x06\x12\x07\n\x03\x45RR\x10\x07'),
    dependencies=[player__pb2.DESCRIPTOR, ])


_TCPPACKET_DISCONNECTPACKET_UPDATE = _descriptor.EnumDescriptor(
    name='Update',
    full_name='TcpPacket.DisconnectPacket.Update',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='NORMAL', index=0, number=0,
            serialized_options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='LOST', index=1, number=1,
            serialized_options=None,
            type=None),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=220,
    serialized_end=250,
)
_sym_db.RegisterEnumDescriptor(_TCPPACKET_DISCONNECTPACKET_UPDATE)

_TCPPACKET_CONNECTPACKET_UPDATE = _descriptor.EnumDescriptor(
    name='Update',
    full_name='TcpPacket.ConnectPacket.Update',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='SELF', index=0, number=0,
            serialized_options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='NEW', index=1, number=1,
            serialized_options=None,
            type=None),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=399,
    serialized_end=426,
)
_sym_db.RegisterEnumDescriptor(_TCPPACKET_CONNECTPACKET_UPDATE)

_TCPPACKET_PACKETTYPE = _descriptor.EnumDescriptor(
    name='PacketType',
    full_name='TcpPacket.PacketType',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='DISCONNECT', index=0, number=0,
            serialized_options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='CONNECT', index=1, number=1,
            serialized_options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='CREATE_LOBBY', index=2, number=2,
            serialized_options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='CHAT', index=3, number=3,
            serialized_options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='PLAYER_LIST', index=4, number=4,
            serialized_options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='ERR_LDNE', index=5, number=5,
            serialized_options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='ERR_LFULL', index=6, number=6,
            serialized_options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='ERR', index=7, number=7,
            serialized_options=None,
            type=None),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=945,
    serialized_end=1069,
)
_sym_db.RegisterEnumDescriptor(_TCPPACKET_PACKETTYPE)


_TCPPACKET_DISCONNECTPACKET = _descriptor.Descriptor(
    name='DisconnectPacket',
    full_name='TcpPacket.DisconnectPacket',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='type', full_name='TcpPacket.DisconnectPacket.type', index=0,
            number=1, type=14, cpp_type=8, label=2,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='player', full_name='TcpPacket.DisconnectPacket.player', index=1,
            number=2, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='update', full_name='TcpPacket.DisconnectPacket.update', index=2,
            number=3, type=14, cpp_type=8, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
        _TCPPACKET_DISCONNECTPACKET_UPDATE,
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=86,
    serialized_end=250,
)

_TCPPACKET_CONNECTPACKET = _descriptor.Descriptor(
    name='ConnectPacket',
    full_name='TcpPacket.ConnectPacket',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='type', full_name='TcpPacket.ConnectPacket.type', index=0,
            number=1, type=14, cpp_type=8, label=2,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='player', full_name='TcpPacket.ConnectPacket.player', index=1,
            number=2, type=11, cpp_type=10, label=2,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='lobby_id', full_name='TcpPacket.ConnectPacket.lobby_id', index=2,
            number=3, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='update', full_name='TcpPacket.ConnectPacket.update', index=3,
            number=4, type=14, cpp_type=8, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
        _TCPPACKET_CONNECTPACKET_UPDATE,
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=253,
    serialized_end=426,
)

_TCPPACKET_CREATELOBBYPACKET = _descriptor.Descriptor(
    name='CreateLobbyPacket',
    full_name='TcpPacket.CreateLobbyPacket',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='type', full_name='TcpPacket.CreateLobbyPacket.type', index=0,
            number=1, type=14, cpp_type=8, label=2,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='lobby_id', full_name='TcpPacket.CreateLobbyPacket.lobby_id', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='max_players', full_name='TcpPacket.CreateLobbyPacket.max_players', index=2,
            number=3, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
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
    syntax='proto2',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=428,
    serialized_end=523,
)

_TCPPACKET_CHATPACKET = _descriptor.Descriptor(
    name='ChatPacket',
    full_name='TcpPacket.ChatPacket',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='type', full_name='TcpPacket.ChatPacket.type', index=0,
            number=1, type=14, cpp_type=8, label=2,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='message', full_name='TcpPacket.ChatPacket.message', index=1,
            number=2, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='player', full_name='TcpPacket.ChatPacket.player', index=2,
            number=3, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='lobby_id', full_name='TcpPacket.ChatPacket.lobby_id', index=3,
            number=4, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
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
    syntax='proto2',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=525,
    serialized_end=634,
)

_TCPPACKET_PLAYERLISTPACKET = _descriptor.Descriptor(
    name='PlayerListPacket',
    full_name='TcpPacket.PlayerListPacket',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='type', full_name='TcpPacket.PlayerListPacket.type', index=0,
            number=1, type=14, cpp_type=8, label=2,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='player_list', full_name='TcpPacket.PlayerListPacket.player_list', index=1,
            number=3, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
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
    syntax='proto2',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=636,
    serialized_end=721,
)

_TCPPACKET_ERRLDNEPACKET = _descriptor.Descriptor(
    name='ErrLdnePacket',
    full_name='TcpPacket.ErrLdnePacket',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='type', full_name='TcpPacket.ErrLdnePacket.type', index=0,
            number=1, type=14, cpp_type=8, label=2,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='err_message', full_name='TcpPacket.ErrLdnePacket.err_message', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
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
    syntax='proto2',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=723,
    serialized_end=796,
)

_TCPPACKET_ERRLFULLPACKET = _descriptor.Descriptor(
    name='ErrLfullPacket',
    full_name='TcpPacket.ErrLfullPacket',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='type', full_name='TcpPacket.ErrLfullPacket.type', index=0,
            number=1, type=14, cpp_type=8, label=2,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='err_message', full_name='TcpPacket.ErrLfullPacket.err_message', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
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
    syntax='proto2',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=798,
    serialized_end=872,
)

_TCPPACKET_ERRPACKET = _descriptor.Descriptor(
    name='ErrPacket',
    full_name='TcpPacket.ErrPacket',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='type', full_name='TcpPacket.ErrPacket.type', index=0,
            number=1, type=14, cpp_type=8, label=2,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='err_message', full_name='TcpPacket.ErrPacket.err_message', index=1,
            number=2, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=_b("").decode('utf-8'),
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
    syntax='proto2',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=874,
    serialized_end=943,
)

_TCPPACKET = _descriptor.Descriptor(
    name='TcpPacket',
    full_name='TcpPacket',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='type', full_name='TcpPacket.type', index=0,
            number=1, type=14, cpp_type=8, label=2,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[_TCPPACKET_DISCONNECTPACKET, _TCPPACKET_CONNECTPACKET, _TCPPACKET_CREATELOBBYPACKET, _TCPPACKET_CHATPACKET,
                  _TCPPACKET_PLAYERLISTPACKET, _TCPPACKET_ERRLDNEPACKET, _TCPPACKET_ERRLFULLPACKET, _TCPPACKET_ERRPACKET, ],
    enum_types=[
        _TCPPACKET_PACKETTYPE,
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=35,
    serialized_end=1069,
)

_TCPPACKET_DISCONNECTPACKET.fields_by_name['type'].enum_type = _TCPPACKET_PACKETTYPE
_TCPPACKET_DISCONNECTPACKET.fields_by_name['player'].message_type = player__pb2._PLAYER
_TCPPACKET_DISCONNECTPACKET.fields_by_name['update'].enum_type = _TCPPACKET_DISCONNECTPACKET_UPDATE
_TCPPACKET_DISCONNECTPACKET.containing_type = _TCPPACKET
_TCPPACKET_DISCONNECTPACKET_UPDATE.containing_type = _TCPPACKET_DISCONNECTPACKET
_TCPPACKET_CONNECTPACKET.fields_by_name['type'].enum_type = _TCPPACKET_PACKETTYPE
_TCPPACKET_CONNECTPACKET.fields_by_name['player'].message_type = player__pb2._PLAYER
_TCPPACKET_CONNECTPACKET.fields_by_name['update'].enum_type = _TCPPACKET_CONNECTPACKET_UPDATE
_TCPPACKET_CONNECTPACKET.containing_type = _TCPPACKET
_TCPPACKET_CONNECTPACKET_UPDATE.containing_type = _TCPPACKET_CONNECTPACKET
_TCPPACKET_CREATELOBBYPACKET.fields_by_name['type'].enum_type = _TCPPACKET_PACKETTYPE
_TCPPACKET_CREATELOBBYPACKET.containing_type = _TCPPACKET
_TCPPACKET_CHATPACKET.fields_by_name['type'].enum_type = _TCPPACKET_PACKETTYPE
_TCPPACKET_CHATPACKET.fields_by_name['player'].message_type = player__pb2._PLAYER
_TCPPACKET_CHATPACKET.containing_type = _TCPPACKET
_TCPPACKET_PLAYERLISTPACKET.fields_by_name['type'].enum_type = _TCPPACKET_PACKETTYPE
_TCPPACKET_PLAYERLISTPACKET.fields_by_name['player_list'].message_type = player__pb2._PLAYER
_TCPPACKET_PLAYERLISTPACKET.containing_type = _TCPPACKET
_TCPPACKET_ERRLDNEPACKET.fields_by_name['type'].enum_type = _TCPPACKET_PACKETTYPE
_TCPPACKET_ERRLDNEPACKET.containing_type = _TCPPACKET
_TCPPACKET_ERRLFULLPACKET.fields_by_name['type'].enum_type = _TCPPACKET_PACKETTYPE
_TCPPACKET_ERRLFULLPACKET.containing_type = _TCPPACKET
_TCPPACKET_ERRPACKET.fields_by_name['type'].enum_type = _TCPPACKET_PACKETTYPE
_TCPPACKET_ERRPACKET.containing_type = _TCPPACKET
_TCPPACKET.fields_by_name['type'].enum_type = _TCPPACKET_PACKETTYPE
_TCPPACKET_PACKETTYPE.containing_type = _TCPPACKET
DESCRIPTOR.message_types_by_name['TcpPacket'] = _TCPPACKET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TcpPacket = _reflection.GeneratedProtocolMessageType('TcpPacket', (_message.Message,), dict(

    DisconnectPacket=_reflection.GeneratedProtocolMessageType('DisconnectPacket', (_message.Message,), dict(
        DESCRIPTOR=_TCPPACKET_DISCONNECTPACKET,
        __module__='tcp_packet_pb2'
        # @@protoc_insertion_point(class_scope:TcpPacket.DisconnectPacket)
    )),

    ConnectPacket=_reflection.GeneratedProtocolMessageType('ConnectPacket', (_message.Message,), dict(
        DESCRIPTOR=_TCPPACKET_CONNECTPACKET,
        __module__='tcp_packet_pb2'
        # @@protoc_insertion_point(class_scope:TcpPacket.ConnectPacket)
    )),

    CreateLobbyPacket=_reflection.GeneratedProtocolMessageType('CreateLobbyPacket', (_message.Message,), dict(
        DESCRIPTOR=_TCPPACKET_CREATELOBBYPACKET,
        __module__='tcp_packet_pb2'
        # @@protoc_insertion_point(class_scope:TcpPacket.CreateLobbyPacket)
    )),

    ChatPacket=_reflection.GeneratedProtocolMessageType('ChatPacket', (_message.Message,), dict(
        DESCRIPTOR=_TCPPACKET_CHATPACKET,
        __module__='tcp_packet_pb2'
        # @@protoc_insertion_point(class_scope:TcpPacket.ChatPacket)
    )),

    PlayerListPacket=_reflection.GeneratedProtocolMessageType('PlayerListPacket', (_message.Message,), dict(
        DESCRIPTOR=_TCPPACKET_PLAYERLISTPACKET,
        __module__='tcp_packet_pb2'
        # @@protoc_insertion_point(class_scope:TcpPacket.PlayerListPacket)
    )),

    ErrLdnePacket=_reflection.GeneratedProtocolMessageType('ErrLdnePacket', (_message.Message,), dict(
        DESCRIPTOR=_TCPPACKET_ERRLDNEPACKET,
        __module__='tcp_packet_pb2'
        # @@protoc_insertion_point(class_scope:TcpPacket.ErrLdnePacket)
    )),

    ErrLfullPacket=_reflection.GeneratedProtocolMessageType('ErrLfullPacket', (_message.Message,), dict(
        DESCRIPTOR=_TCPPACKET_ERRLFULLPACKET,
        __module__='tcp_packet_pb2'
        # @@protoc_insertion_point(class_scope:TcpPacket.ErrLfullPacket)
    )),

    ErrPacket=_reflection.GeneratedProtocolMessageType('ErrPacket', (_message.Message,), dict(
        DESCRIPTOR=_TCPPACKET_ERRPACKET,
        __module__='tcp_packet_pb2'
        # @@protoc_insertion_point(class_scope:TcpPacket.ErrPacket)
    )),
    DESCRIPTOR=_TCPPACKET,
    __module__='tcp_packet_pb2'
    # @@protoc_insertion_point(class_scope:TcpPacket)
))
_sym_db.RegisterMessage(TcpPacket)
_sym_db.RegisterMessage(TcpPacket.DisconnectPacket)
_sym_db.RegisterMessage(TcpPacket.ConnectPacket)
_sym_db.RegisterMessage(TcpPacket.CreateLobbyPacket)
_sym_db.RegisterMessage(TcpPacket.ChatPacket)
_sym_db.RegisterMessage(TcpPacket.PlayerListPacket)
_sym_db.RegisterMessage(TcpPacket.ErrLdnePacket)
_sym_db.RegisterMessage(TcpPacket.ErrLfullPacket)
_sym_db.RegisterMessage(TcpPacket.ErrPacket)


# @@protoc_insertion_point(module_scope)
