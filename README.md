This is the PGP signature in python for lan 

Squrril mail and mailman integrator


The Modules are to be installed on mailman and squrrill mail

squrril mail adds the signature and sends the mail to Mailman which searches the lan key-store for the users key.

Mailman verifys the signature and forwards this to the moderator

If the IP is spoofed, The mailman rejects the mail and moderator is safe.

