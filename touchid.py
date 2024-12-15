from LocalAuthentication import LAContext, LAPolicyDeviceOwnerAuthenticationWithBiometrics
from PyObjCTools.AppHelper import runEventLoop, stopEventLoop
import sys

context = LAContext.alloc().init()
reason = "Authenticate with Touch ID"

success, error = context.canEvaluatePolicy_error_(LAPolicyDeviceOwnerAuthenticationWithBiometrics, None)
if success:
    def callback(_success, _error):
        if _success:
            print("Authenticated with Touch ID!")
        else:
            print("Authentication failed:", _error)

        # Instead of sys.exit(), stop the event loop:
        stopEventLoop()

    context.evaluatePolicy_localizedReason_reply_(LAPolicyDeviceOwnerAuthenticationWithBiometrics, reason, callback)
    # This will block until stopEventLoop() is called:
    runEventLoop()

    # Once runEventLoop() returns, you can now safely exit.
    sys.exit(0)

else:
    print("Touch ID not available")
    print("Error:", error)
    # If you want to exit here:
    sys.exit(1)