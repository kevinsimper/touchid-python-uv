from Security import (
    SecAccessControlCreateWithFlags,
    kSecAttrAccessibleWhenPasscodeSetThisDeviceOnly,
    kSecAttrAccessControl,
    kSecAttrAccount,
    kSecAttrService,
    kSecClass,
    kSecClassGenericPassword,
    kSecValueData,
    SecItemAdd,
    SecCopyErrorMessageString,
    errSecSuccess,
)
import objc

# Create access control with user presence requirement
flags = 1 << 2  # Equivalent to SecAccessControlCreateFlags.userPresence
access_control = SecAccessControlCreateWithFlags(
    None,  # CFAllocatorRef (use default)
    kSecAttrAccessibleWhenPasscodeSetThisDeviceOnly,  # Accessibility
    flags,  # Authentication requirement
    None  # CFErrorRef (not used here)
)

if not access_control:
    print("Access control creation failed.")
    exit(1)

# Define keychain attributes
account = "test_account"
service = "test_service"
password = b"my_secure_password"  # Must be bytes

# Store the item with access control
query = {
    kSecClass: kSecClassGenericPassword,
    kSecAttrAccount: account,
    kSecAttrService: service,
    kSecValueData: password,
    kSecAttrAccessControl: access_control,  # Use access control to enforce Touch ID
}

# Add the item to the keychain
status, _ = SecItemAdd(query, None)

if status == errSecSuccess:
    print("Keychain item added successfully!")
else:
    # Retrieve error message for debugging
    error_message = SecCopyErrorMessageString(status, None)
    error_message_str = str(error_message) if error_message else "Unknown error"
    print(f"Failed to add keychain item. Status: {status}, Error: {error_message_str}")