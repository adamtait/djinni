// AUTOGENERATED FILE - DO NOT MODIFY!
// This file generated by Djinni from user_token.djinni

#pragma once

#include "djinni_support.hpp"
#include "user_token.hpp"

namespace djinni_generated {

class NativeUserToken final : ::djinni::JniInterface<::UserToken, NativeUserToken> {
public:
    using CppType = std::shared_ptr<::UserToken>;
    using JniType = jobject;

    using Boxed = NativeUserToken;

    ~NativeUserToken();

    static CppType toCpp(JNIEnv* jniEnv, JniType j) { return ::djinni::JniClass<NativeUserToken>::get()._fromJava(jniEnv, j); }
    static ::djinni::LocalRef<JniType> fromCpp(JNIEnv* jniEnv, const CppType& c) { return {jniEnv, ::djinni::JniClass<NativeUserToken>::get()._toJava(jniEnv, c)}; }

private:
    NativeUserToken();
    friend ::djinni::JniClass<NativeUserToken>;
    friend ::djinni::JniInterface<::UserToken, NativeUserToken>;

    class JavaProxy final : ::djinni::JavaProxyCacheEntry, public ::UserToken
    {
    public:
        JavaProxy(JniType j);
        ~JavaProxy();

        std::string whoami() override;

    private:
        using ::djinni::JavaProxyCacheEntry::getGlobalRef;
        friend ::djinni::JniInterface<::UserToken, ::djinni_generated::NativeUserToken>;
        friend ::djinni::JavaProxyCache<JavaProxy>;
    };

    const ::djinni::GlobalRef<jclass> clazz { ::djinni::jniFindClass("com/dropbox/djinni/test/UserToken") };
    const jmethodID method_whoami { ::djinni::jniGetMethodID(clazz.get(), "whoami", "()Ljava/lang/String;") };
};

}  // namespace djinni_generated