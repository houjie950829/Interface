# coding=utf-8
import hashlib


def roles(phone, numes):
    """注册加密规则"""
    try:
        p1 = phone[:3]
        p2 = phone[3:6]
        p3 = phone[6:9]
        p4 = phone[9:11]
        n1 = numes[:1]
        n2 = numes[1:2]
        n3 = numes[2:3]
        n4 = numes[3:4]
        p1_1 = p1[::-1] + n1
        p2_1 = p2[::-1] + n2
        p3_1 = p3[::-1] + n3
        p4_1 = p4[::-1] + n4
        role_number = p1_1 + p2_1 + p3_1 + p4_1
        role_number = '1' + role_number
        role_number = int(role_number) - int(numes) * int(numes)
        # print(role_number)
        return str(role_number)
    except Exception as msges:
        print(msges)


def md5test(encryptio):
    try:
        md = hashlib.md5()
        sign_bytes_utf8 = encryptio.encode(encoding="utf-8")
        md.update(sign_bytes_utf8)
        sign_md5 = md.hexdigest()
        return sign_md5
    except Exception as msges:
        print(msges)


class encryption(object):
    u"""md5加密"""

    @staticmethod
    def md5_token(phone, numes):
        u"""手机号和验证码已一定的规则加密"""
        encrypted = roles(phone, numes)
        return md5test(encrypted)


if __name__ == '__main__':
    md5 = encryption()
    b = md5.md5_token('15102823933', '1234')
    print(b)
