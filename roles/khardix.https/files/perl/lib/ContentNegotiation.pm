#!/usr/bin/env perl
package ContentNegotiation;

use strict;
use warnings;
use Locale::Util qw(parse_http_accept_language);
use List::MoreUtils qw(any);

sub accept_language {
    my $header = shift;
    my @supported = @_;

    my @accepted = parse_http_accept_language $header;
    foreach my $lang (@accepted) {
        if (any { $_ eq $lang } @supported) {
            return $lang;
        }
    }
    return shift @supported;
}

1;
__END__
