use strict;
use warnings;

use Test::Simple tests => 2;

use ContentNegotiation qw(accept_lang);


ok( ContentNegotiation::accept_lang('cs,en-US;q=0.7,en;q=0.3', 'en', 'cs') eq 'cs');
ok( ContentNegotiation::accept_lang('ru,fr;q=0.5', 'en', 'cs') eq 'en');
