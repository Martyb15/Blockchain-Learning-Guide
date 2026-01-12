// phase 1 hashing 
#include <iostream> 
#include <sstream> 
#include <iomanip>
#include <string> 
#include <openssl/sha.h> 

std::string SHA256(const std::string& data) { 
    unsigned char hash[SHA256_192_DIGEST_LENGTH];
    SHA256(reinterpret_cast<const unsigned char*>(data.c_str()), 
        data.size(), hash);

    
}