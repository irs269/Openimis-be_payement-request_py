class SendPaytRequestMutation(OpenIMISMutation):
	@classmethod
    def async_mutate(cls, user, **data):
        try:
            //Code python faisant appel au Webservice pour d'initier la demande de paiement
            return None
        except Exception as exc:
            logger.exception("payment_request.mutation.failed_to_send_request")
            return [{
                'message': _("payment_request.mutation.failed_to_send_request"),
                'detail': str(exc)}
            ]
