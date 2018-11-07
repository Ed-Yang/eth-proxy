import stratum.custom_exceptions # Python3
from twisted.internet import defer
from stratum.services import wrap_result_object # Python3

class GenericEventHandler(object):
    def _handle_event(self, msg_method, msg_result, connection_ref):
        return defer.maybeDeferred(wrap_result_object, self.handle_event(msg_method, msg_result, connection_ref))
    
    def handle_event(self, msg_method, msg_params, connection_ref):
        '''In most cases you'll only need to overload this method.'''
        print ("Other side called method", msg_method, "with params", msg_params) # Python3
        raise custom_exceptions.MethodNotFoundException("Method '%s' not implemented" % msg_method)