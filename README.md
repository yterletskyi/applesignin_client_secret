# applesignin_client_secret

Creates an ES256 token and signs using the ECDSA with the P-256 curve and the SHA-256 hash algorithm.

Use to create a `client_secret` for Apple Sign In:
https://developer.apple.com/documentation/signinwithapplerestapi/generate_and_validate_tokens

To generate a client secret:
- Add a `.p8` private key file from apple developer dashboard to the root directory.
- Add a `defaults.cfg` configuration file to the root directory where provide: `key_id`, `key_path`, `team_id` and `client_id` values.
