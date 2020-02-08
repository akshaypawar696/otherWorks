import zlib

teststr = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus
pretium justo eget elit eleifend, et dignissim quam eleifend. Nam vehicula nisl
posuere velit volutpat, vitae scelerisque nisl imperdiet. Phasellus dignissim,
dolor amet."""

cmpstr = zlib.compress(teststr.encode('utf-8'))
print(len(cmpstr))

uncmpstr = zlib.decompress(cmpstr)
print(len(uncmpstr))