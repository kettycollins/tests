def get_permutation_order(phrase):
    """Generates the permutation order based on the provided phrase."""
    order = sorted(range(len(phrase)), key=lambda x: phrase[x])
    return order

def encrypt(text, order):
    """Encrypts the text using a simple permutation."""
    # Prepare the text by removing spaces
    text = text.replace(" ", "")
    
    # Fill the text with spaces if needed
    while len(text) % len(order) != 0:
        text += ' '

    encrypted_text = [''] * len(text)
    # Encrypt the text
    for i in range(0, len(text), len(order)):
        for j, index in enumerate(order):
            encrypted_text[i + j] = text[i + index]

    return ''.join(encrypted_text)

def decrypt(encrypted_text, order):
    """Decrypts the text using a simple permutation."""
    decrypted_text = [''] * len(encrypted_text)
    # Decrypt the text
    for i in range(0, len(encrypted_text), len(order)):
        for j, index in enumerate(order):
            decrypted_text[i + index] = encrypted_text[i + j]

    return ''.join(decrypted_text)

def permute(text, order):
    """Applies permutation to the text according to the order."""
    permuted_text = [''] * len(text)
    
    # Add text characters to the permuted array
    for i, index in enumerate(order):
        if i < len(text):  # Check bounds
            permuted_text[index] = text[i]
    
    return ''.join(permuted_text)

def encrypt_double_permutation(text, key1, key2):
    """Encrypts the text using double permutation with two keys."""
    # Generate permutation order for both keys
    order1 = get_permutation_order(key1)
    order2 = get_permutation_order(key2)

    # First permutation
    first_permutation = permute(text, order1)
    # Second permutation
    encrypted_text = permute(first_permutation, order2)
    
    return encrypted_text

def decrypt_double_permutation(encrypted_text, key1, key2):
    """Decrypts the text using double permutation with two keys."""
    # Generate permutation order for both keys
    order1 = get_permutation_order(key1)
    order2 = get_permutation_order(key2)

    # Reverse order for both keys
    reverse_order1 = sorted(range(len(order1)), key=lambda x: order1[x])
    reverse_order2 = sorted(range(len(order2)), key=lambda x: order2[x])

    # First reverse permutation
    first_decryption = permute(encrypted_text, reverse_order2)
    # Second reverse permutation
    decrypted_text = permute(first_decryption, reverse_order1)
    
    return decrypted_text

# Main part of the program
if __name__ == "__main__":
    original_text = """The artist is the creator of beautiful things. To reveal art and conceal the artist is art's aim. 
    The critic is he who can translate into another manner or a new material his impression of beautiful things. 
    The highest, as the lowest, form of criticism is a mode of autobiography. Those who find ugly meanings in beautiful things 
    are corrupt without being charming. This is a fault. Those who find beautiful meanings in beautiful things are the cultivated. 
    For these there is hope. They are the elect to whom beautiful things mean only Beauty. There is no such thing as a moral or an immoral book. 
    Books are well written, or badly written. That is all. The nineteenth-century dislike of realism is the rage of Caliban seeing his own face in a glass. 
    The nineteenth-century dislike of Romanticism is the rage of Caliban not seeing his own face in a glass. 
    The moral life of man forms part of the subject matter of the artist, but the morality of art consists in the perfect use of an imperfect medium. 
    No artist desires to prove anything. Even things that are true can be proved. No artist has ethical sympathies. 
    An ethical sympathy in an artist is an unpardonable mannerism of style. No artist is ever morbid. The artist can express everything. 
    Thought and language are to the artist instruments of an art. Vice and virtue are to the artist materials for an art. 
    From the point of view of form, the type of all the arts is the art of the musician. From the point of view of feeling, the actor's craft is the type. 
    All art is at once surface and symbol. Those who go beneath the surface do so at their peril. Those who read the symbol do so at their peril. 
    It is the spectator, and not life, that art really mirrors. Diversity of opinion about a work of art shows that the work is new, complex, vital. 
    When critics disagree the artist is in accord with himself. We can forgive a man for making a useful thing as long as he does not admire it. 
    The only excuse for making a useless thing is that one admires it intensely. All art is quite useless."""

    # Generate permutation order based on the first key phrase
    key_phrase1 = "SECRET"
    permutation_order1 = get_permutation_order(key_phrase1)

    # Encrypt the original text with the first key
    encrypted_text1 = encrypt(original_text, permutation_order1)
    print("Encrypted text using first permutation (SECRET):")
    print(encrypted_text1)

    #second permutation with the key "CRYPTO"
    key_phrase2 = "CRYPTO"
    encrypted_text_double = encrypt_double_permutation(encrypted_text1, key_phrase1, key_phrase2)
    print("\nEncrypted text after applying second permutation (CRYPTO):")
    print(encrypted_text_double)

    # Decrypt the text back using double permutation
    decrypted_text_double = decrypt_double_permutation(encrypted_text_double, key_phrase1, key_phrase2)
    print("\nDecrypted text after reversing double permutation:")
    print(decrypted_text_double)

    decrypted_text = decrypt(decrypted_text_double, permutation_order1)
    print("\nDecrypted text after reversing first permutation:")
    print(decrypted_text)
