$.inplaceeditform.extend(
    {
        inplaceApplySuccessShowMessage: function(inplace_span) {
            var self = $.inplaceeditform;
            if (self.opts.successText) {
                var modal = $('#inplaceedit-modal');
                var body = modal.find('div.modal-body p');
                body.html(self.opts.successText);

                setTimeout(function () {
                    modal.fadeOut(function () {
                        $(this).remove();
                    });

                    // $.ajax({
                    //     type: 'POST',
                    //     url: '/front-api/reload-sections',
                    //     data: (),
                    //     success: function (data) {
                    //         sections(data)
                    //     },
                    //     error: function (data) {
                    //         ajaxError()
                    //    }
                    // });

                }, 2000);
            }
            modal.show();
        }
    }
);
