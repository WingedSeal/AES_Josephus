import aesjosephus as aj

print(aj.encrypt("abcd", "abcd", aj.Mode.ORIGINAL).to_string())
