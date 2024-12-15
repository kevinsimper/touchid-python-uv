from Security import (
    SecItemCopyMatching,
    kSecClass,
    kSecClassGenericPassword,
    kSecAttrAccount,
    kSecAttrService,
    kSecReturnData,
    kSecUseOperationPrompt,
    errSecSuccess,
)

retrieve_query = {
    kSecClass: kSecClassGenericPassword,
    kSecAttrAccount: "test_account",
    kSecAttrService: "test_service",
    kSecReturnData: True,
    kSecUseOperationPrompt: "Authenticate to retrieve your secure password"
}

status, retrieved_data = SecItemCopyMatching(retrieve_query, None)

if status == errSecSuccess:
    print("Retrieved data:", retrieved_data)
else:
    print("Failed to retrieve item:", status)