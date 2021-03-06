define(['utils/utils'], function (Utils) {
    'use strict';

    describe('Utils', function () {
        it('should return node attributes', function () {
            var actualAttributes,
                element;

            // create your node with attributes
            element = document.createElement('div');
            element.setAttribute('attribute', 'myAttribute');
            element.setAttribute('data-type', 'my-data-type');
            element.setAttribute('data-category', 'my-data-category');
            element.setAttribute('data-event', 'my-data-event');

            actualAttributes = Utils.getNodeProperties(element.attributes);
            expect(actualAttributes).toEqual({
                attribute: 'myAttribute',
                'data-type': 'my-data-type',
                'data-category': 'my-data-category',
                'data-event': 'my-data-event'
            });

            actualAttributes = Utils.getNodeProperties(element.attributes,
                'data-');
            expect(actualAttributes).toEqual({
                'type': 'my-data-type',
                'category': 'my-data-category',
                'event': 'my-data-event'
            });

            actualAttributes = Utils.getNodeProperties(element.attributes,
                'data-', ['data-type', 'data-category']);
            expect(actualAttributes).toEqual({
                'event': 'my-data-event'
            });
        });

        it('should return node attributes', function () {
            expect(Utils.formatDate('2014-01-31')).toEqual('January 31, 2014');
            expect(Utils.formatDate('2014-01-01')).toEqual('January 1, 2014');
        });

    });

    describe('formatDisplayPercentage', function () {
        it('should return < 1% if the parameter is < 0.01', function () {
            expect(Utils.formatDisplayPercentage(0)).toEqual('< 1%');
            expect(Utils.formatDisplayPercentage(0.002)).toEqual('< 1%');
        });

        it('should return a percentage formatted to a single decimal place if the parameter is >= 0.01', function () {
            expect(Utils.formatDisplayPercentage(0.01)).toEqual('1.0%');
            expect(Utils.formatDisplayPercentage(0.396)).toEqual('39.6%');
            expect(Utils.formatDisplayPercentage(1)).toEqual('100.0%');
        });
    });
});
